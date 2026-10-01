# Home

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-opensource/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-opensource/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-opensource/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-opensource/actions/workflows/release.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-opensource/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-opensource)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![CICDLinter](https://img.shields.io/badge/CI/CD-actionlint-blue)](https://github.com/rhysd/actionlint)
[![CICDSecurityChecker](https://img.shields.io/badge/CI/CD--security-zizmor-yellow)](https://github.com/zizmorcore/zizmor)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![EndOfFileFormatter](https://img.shields.io/badge/EOF-end--of--file--fixer-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![EndOfLineFormatter](https://img.shields.io/badge/EOL-mixed--line--ending-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![JSONFormatter](https://img.shields.io/badge/JSON-pretty--format--json-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![JSONLinter](https://img.shields.io/badge/JSON-check--json-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![LargeFileChecker](https://img.shields.io/badge/large--files-check--added--large--files-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![MarkdownLinter](https://img.shields.io/badge/Markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![MergeConflictChecker](https://img.shields.io/badge/merge--conflict-check--merge--conflict-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![ModuleTestNamingChecker](https://img.shields.io/badge/test--naming-name--tests--test-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![ShellFormatter](https://img.shields.io/badge/shell-shfmt-orange)](https://github.com/mvdan/sh)
[![ShellLinter](https://img.shields.io/badge/shell-shellcheck-blue)](https://github.com/koalaman/shellcheck)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TOMLLinter](https://img.shields.io/badge/TOML-tombi-blueviolet)](https://github.com/tombi-toml/tombi)
[![TrailingWhitespaceFormatter](https://img.shields.io/badge/whitespace-trailing--whitespace--fixer-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![YAMLLinter](https://img.shields.io/badge/YAML-ryl-red)](https://github.com/owenlamont/ryl)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-opensource?style=social)](https://github.com/Winipedia/pyrig-opensource)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/Documentation-zensical-326CE5)](https://Winipedia.github.io/pyrig-opensource)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-opensource?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-opensource)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-opensource)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-opensource)](https://github.com/Winipedia/pyrig-opensource/blob/main/LICENSE)

---

> A pyrig plugin that combines other pyrig plugins for open-source projects.

---

## Overview

Drop-in [pyrig](https://github.com/Winipedia/pyrig) plugin that bundles the
plugins recommended for a public, open-source project into a single
dependency:

- [`pyrig-codecov`](https://github.com/Winipedia/pyrig-codecov) — uploads
  coverage reports to Codecov.
- [`pyrig-codeql`](https://github.com/Winipedia/pyrig-codeql) — enables
  GitHub CodeQL security scanning.
- [`pyrig-fixtures`](https://github.com/Winipedia/pyrig-fixtures) — shares
  pytest fixtures across dependent packages.
- [`pyrig-public`](https://github.com/Winipedia/pyrig-public) — configures
  GitHub features for public repositories.
- [`pyrig-pypi`](https://github.com/Winipedia/pyrig-pypi) — publishes
  releases to PyPI.

No configuration required — installing the package as a development dependency
is the whole setup. Then regenerate your pyrig configs as usual. Each bundled
plugin's overrides are picked up automatically.

## Installation

```bash
uv add pyrig-opensource --dev
uv run pyrig sync
```

## Usage

```bash
uv run pyrig-opensource plugins
```

Prints every plugin bundled by this plugin, one per line, so you can confirm
what got installed.

## How it works

The plugin declares `pyrig`, `pyrig-codecov`, `pyrig-codeql`,
`pyrig-fixtures`, `pyrig-public`, and `pyrig-pypi` as runtime dependencies, so
installing it transitively installs and activates each one's overrides. It
adds no overrides of its own beyond the `plugins` CLI command, which reports
the bundled plugins from a hand-maintained list.

## API Reference

For class- and method-level details, see the [API Reference](api.md), generated
automatically from the source.
