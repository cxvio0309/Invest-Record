from __future__ import annotations

import argparse
from datetime import datetime, timezone

from invest_record.db import connect, initialize_schema


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Invest-Record CLI")
    parser.add_argument("--db-path", help="Path to the SQLite database file.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize the database.")
    init_parser.set_defaults(func=handle_init)

    add_parser = subparsers.add_parser("add", help="Add a transaction.")
    add_parser.add_argument("--asset", required=True)
    add_parser.add_argument("--type", required=True, dest="txn_type")
    add_parser.add_argument("--quantity", type=float, required=True)
    add_parser.add_argument("--price", type=float, required=True)
    add_parser.add_argument("--currency", required=True)
    add_parser.add_argument("--traded-at", dest="traded_at")
    add_parser.add_argument("--notes")
    add_parser.set_defaults(func=handle_add)

    list_parser = subparsers.add_parser("list", help="List transactions.")
    list_parser.set_defaults(func=handle_list)

    return parser


def handle_init(args: argparse.Namespace) -> None:
    with connect(args.db_path) as connection:
        initialize_schema(connection)
    print("Database initialized.")


def handle_add(args: argparse.Namespace) -> None:
    traded_at = args.traded_at or datetime.now(timezone.utc).isoformat()
    with connect(args.db_path) as connection:
        initialize_schema(connection)
        connection.execute(
            """
            INSERT INTO transactions (asset, txn_type, quantity, price, currency, traded_at, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                args.asset,
                args.txn_type,
                args.quantity,
                args.price,
                args.currency,
                traded_at,
                args.notes,
            ),
        )
        connection.commit()
    print("Transaction added.")


def handle_list(args: argparse.Namespace) -> None:
    with connect(args.db_path) as connection:
        initialize_schema(connection)
        rows = connection.execute(
            """
            SELECT id, asset, txn_type, quantity, price, currency, traded_at, notes
            FROM transactions
            ORDER BY traded_at DESC
            """
        ).fetchall()

    if not rows:
        print("No transactions found.")
        return

    for row in rows:
        print(
            f"#{row['id']} {row['traded_at']} {row['asset']} "
            f"{row['txn_type']} {row['quantity']} @ {row['price']} {row['currency']}"
            + (f" ({row['notes']})" if row["notes"] else "")
        )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
