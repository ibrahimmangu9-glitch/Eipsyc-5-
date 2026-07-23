# Contributing to EIPSYC5 AFRICA

Thank you for your interest in contributing to EIPSYC5 AFRICA! This document provides guidelines for contributing.

## Code Style

### Python (Backend)
- Follow PEP 8
- Use type hints for all functions
- Use black for formatting
- Use isort for imports

```bash
black app/
isort app/
pylint app/
mypy app/
```

### TypeScript/React (Frontend)
- Use ESLint + Prettier
- Type everything (no `any`)
- Component naming: PascalCase
- Hooks: camelCase

```bash
npm run lint
npm run format
npm run type-check
```

## Testing Requirements

### Backend
```bash
pytest tests/ --cov=app --cov-report=html
```
- Minimum 80% code coverage

### Frontend
```bash
npm run test -- --coverage
```
- Minimum 70% code coverage

## Branch Naming
- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation
- `refactor/description` - Code refactoring

## Commit Messages
- Start with verb: "Add", "Fix", "Update", "Remove"
- Be descriptive but concise
- Example: "Add country search to explore page"

## Pull Request Process

1. Ensure all tests pass
2. Update documentation
3. Create descriptive PR title
4. Link related issues
5. Request review from maintainers
6. Address review comments

## Database Migrations

When modifying schema:

```bash
cd backend
alembic revision --autogenerate -m "Description"
alembic upgrade head
```

## Security

- Never commit secrets or credentials
- Use environment variables for configuration
- Validate all user input
- Use parameterized queries (SQLAlchemy ORM)
- Add authentication checks to protected endpoints

## Questions?

Create a GitHub issue or discussion.

Welcome to the team! 🚀
