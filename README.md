# ezmsg.org Documentation Site

This repository hosts the main documentation site for the ezmsg ecosystem, published at [ezmsg.org](https://ezmsg.org).

## Overview

This is an **organization-level documentation site** that provides:
- Getting started guides and tutorials
- Conceptual explanations of ezmsg architecture
- How-to guides for common use cases
- Links to API documentation for all ezmsg packages
- Developer guides for contributors
- Information about ezmsg extensions

## Documentation Architecture

The ezmsg documentation is distributed across multiple repositories:

- **ezmsg.org** (this repo) → General documentation, tutorials, guides
- **ezmsg.org/ezmsg** → Core ezmsg API reference (from [ezmsg repo](https://github.com/ezmsg-org/ezmsg))
- **ezmsg.org/ezmsg-sigproc** → Signal processing API (from [ezmsg-sigproc repo](https://github.com/ezmsg-org/ezmsg-sigproc))
- **ezmsg.org/ezmsg-lsl** → LSL integration API (from [ezmsg-lsl repo](https://github.com/ezmsg-org/ezmsg-lsl))
- **ezmsg.org/ezmsg-learn** → Machine learning API (from [ezmsg-learn repo](https://github.com/ezmsg-org/ezmsg-learn))

Each package repository builds its own API documentation using autodoc from docstrings, while this repository contains the narrative documentation.

## Building Documentation Locally

### Prerequisites
- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Build Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ezmsg-org/ezmsg-org.github.io.git
   cd ezmsg-org.github.io
   ```

2. **Install dependencies**
   ```bash
   uv sync --only-group docs
   ```

3. **Build the documentation**
   ```bash
   cd docs
   uv run make html
   ```

4. **View the documentation**
   Open `docs/build/html/index.html` in your browser

### Clean Build
To rebuild from scratch:
```bash
cd docs
uv run make clean
uv run make html
```

## Contributing

Contributions to improve the documentation are welcome! Please:

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Test the build locally
5. Submit a pull request

### Content Guidelines

- **Tutorials**: Step-by-step guides for beginners
- **How-tos**: Task-oriented guides for specific problems
- **Explanations**: Conceptual information about ezmsg architecture
- **Reference**: Links to API documentation (do not duplicate API docs here)

## Deployment

Documentation is automatically built and deployed via GitHub Actions:

- **Push to `main`**: Automatically deploys to ezmsg.org
- **Pull requests**: Build-only (no deployment) for validation

The workflow is defined in `.github/workflows/docs.yml`.

## Directory Structure

```
ezmsg-org.github.io/
├── .github/
│   └── workflows/
│       └── docs.yml          # GitHub Actions workflow
├── docs/
│   ├── source/
│   │   ├── conf.py           # Sphinx configuration
│   │   ├── index.rst         # Homepage
│   │   ├── tutorials/        # Tutorial content
│   │   ├── how-tos/          # How-to guides
│   │   ├── explanations/     # Conceptual docs
│   │   ├── reference/        # API links and glossary
│   │   ├── developer/        # Contributor guides
│   │   └── extensions/       # Extension information
│   ├── Makefile
│   └── make.bat
├── pyproject.toml            # Python dependencies
└── README.md                 # This file
```

## License

This documentation is part of the ezmsg project. See [LICENSE](LICENSE) for details.

## Support

- **Issues**: Report documentation issues in this repository's [issue tracker](https://github.com/ezmsg-org/ezmsg-org.github.io/issues)
- **Code issues**: Report to the respective package repository

## Acknowledgments

The ezmsg project is supported by Johns Hopkins University (JHU), the JHU Applied Physics Laboratory (APL), the Wyss Center for Bio and Neuro Engineering, and Blackrock Neurotech.
