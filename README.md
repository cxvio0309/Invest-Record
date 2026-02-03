# Invest-Record

Invest-Record is a lightweight local-first tool for recording investment transactions
and reviewing your historical activity. It focuses on a simple CLI and a local SQLite
database so you can start logging trades without additional services.

## Goals
- Record buys/sells/dividends with timestamps and notes.
- Keep data local in a SQLite database.
- Provide a minimal CLI to add and review transactions.

## Development Phases (Roadmap)
1. **Phase 1 - Data foundation + CLI MVP**
   - Define the database schema for transactions.
   - Build CLI commands to initialize the database, add transactions, and list them.
2. **Phase 2 - Reporting**
   - Add basic summaries (per-asset totals, realized P/L).
   - Export transactions to CSV.
3. **Phase 3 - Portfolio insights**
   - Track holdings and average cost.
   - Add simple dashboards (optional TUI/Web UI).
4. **Phase 4 - Quality + automation**
   - Tests, documentation polish, and packaging improvements.

## Quick Start
```bash
python -m invest_record.cli init
python -m invest_record.cli add --asset AAPL --type buy --quantity 10 --price 150 --currency USD
python -m invest_record.cli list
```

## Data Location
By default, the database is stored in `~/.invest-record/invest.db`. You can override
this path with `--db-path` on CLI commands.
