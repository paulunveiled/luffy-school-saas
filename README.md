# luffy-school-saas
This Project is still being built.

**Before changing anything in `results`, read [docs/operating-rules.md](docs/operating-rules.md).**
It is the seven rules Phase 1 established, each with the mistake that taught it.

Per-area design notes live in [`docs/`](docs/).

The working history behind them: session records, control runs and review output; is kept out of this repository, in the private [`luffy-school-saas-history`](https://github.com/adedejimakinde/luffy-school-saas-history) repository (the link 404s without access).

## Codespace Demo Mode

To test locally on a single host (e.g., inside a Codespace), you can enable Demo Mode to bypass the separate security portal address for sign-in.

1. Map `localhost` to the `sunrise_demo` tenant.
2. Set `DEMO_SINGLE_HOST=1` in your `.env` file.
3. Run `python manage.py runserver`.
