# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Add Wagtail 7.4 LTS support
### Changed
### Fixed
### Removed
- Drop support for EOL Wagtail 6.3 LTS
- Drop support for EOL Wagtail 7.2

## [1.8.1] - 2026-04-12
### Fixed
- Revert pip caching in CI as it caused test suite to break (@marteinn)

## [1.8.0] - 2026-04-12
### Added
- Add Python 3.14 support (@marteinn)
- Add Django 6.0 support (@marteinn)
- Add Wagtail 7.3 support (@marteinn)

### Fixed
- Fix potential xss vulnerability in PolyfillColorInputWidget by escaping field id (@marteinn)
- Remove dead code for Wagtail < 6.0 support (@marteinn)
- Pin all GitHub Actions to commit SHAs and upgrade psf/black from 22.3.0 to 26.3.1 (@marteinn)
- Add top-level read-only permissions to GitHub Actions workflow (@marteinn)
- Require environment approval for PyPI publish in GitHub Actions workflow (@marteinn)
- Restrict GitHub Actions push trigger to main branches and release tags (@marteinn)
- Pin isort to specific version in CI (@marteinn)
- Fix broken jQuery selector in PolyfillColorInputWidget caused by missing # prefix after XSS fix (@marteinn)
- Only run publish job in CI on tag pushes (@marteinn)
- Update actions/checkout and actions/setup-python actions to latest version (@marteinn)
- Cache pip dependencies in CI test job (@marteinn)

### Removed
- Drop support for EOL python 3.9 (@marteinn)
- Drop Django 5.1 support (@marteinn)
- Drop Wagtail 7.1 support (@marteinn)

## [1.7.1] - 2025-11-23
### Changed
- Mark PolyfillColorPanel as deprecated and will be removed in v2.0.0 (@marteinn)
- Exclude development files from release build (@marteinn)
- Add package description (@marteinn)
- Add project urls in setup (@marteinn)

### Fixed
- Drop deprecated tests_require in favor of extras_require/test (@marteinn)
- Drop MIT classifier in favor of setup.license MIT (@marteinn)
- Fix invalid include in manifest (@marteinn)
- Drop redundant setup_requires from setup (@marteinn)

## [1.7.0] - 2025-11-22
### Added
- Add support for Wagtail 7.2 (@marteinn)
- Add support for Wagtail 7.1 (@nickmoreton, @tombreit)
- Add support for Wagtail 7.0 (@nickmoreton)

### Changed
- Add CI testing for 7.0 (@nickmoreton)
- Add CI testing for Django 5.2 (@nickmoreton)
- Add test page model for polyfill field (@marteinn)
- Add docker environment for local development (@marteinn)

### Fixed
- Fix incorrect WAGTAIL_SITE_NAME in settings (@marteinn)
- Add WAGTAILADMIN_BASE_URL in settings (@marteinn)
- Ignore local sqlite files (@marteinn)
- Fix STATIC_ROOT warning when running local dev (@marteinn)
- Ignore staticfils dir (@marteinn)
- Ignore local claude config (@marteinn)

### Removed
- Drop support for EOL Wagtail 5.2 (@marteinn)
- Drop support for EOL Wagtail 6.4 (@marteinn)
- Drop Wagtail testing for 5.0 (@nickmoreton)
- Drop Django testing for 5.0 (@nickmoreton)

## [1.6.0] - 2025-01-26
### Added
- Add Wagtail 6.x support (@katdom13)
- Add Python 3.11 support (@katdom13)

### Changed
- Apply Django 5.0 upgrade considerations (@katdom13)

### Removed
- Drop Wagtail < 5.2 support (@katdom13)

## [1.5.0] - 2023-12-22
### Added
- Add Wagtail >= 5.0 support (@katdom13)
- Add Python 3.11 support (@katdom13)

### Removed
- Drop Wagtail < 4.1 support (@katdom13)
- Drop Django 4.0 support (@katdom13)
- Drop Python 3.7 support (@katdom13)

## [1.4.1] - 2023-02-19
### Added
- Add Wagtail 4.1 and 4.2 support (@marteinn)

### Fixed
- Add github issue template

### Removed
- Drop Wagtail 2.16 support (@marteinn)

## [1.4.0] - 2022-07-03
### Added
- Add support for Wagtail 3.0 (@BrianXu20)

### Removed
- Drop support for all Wagtail versions before 2.15 (@BrianXu20)

## [1.3.1] - 2022-01-08
### Added
- Add Python 3.10 support
- Add Wagtail 2.14 and 2.15 support

### Removed
- Drop Python 3.6 support

## [1.3.0] - 2021-09-27
### Added
- Add support for Wagtail 2.13+ (@marts)

### Removed
- Drop support for Wagtail 2.12 and older

## [1.2.0] - 2020-01-10
### Added
- Add additional text field for handling color values manually (@marts)
