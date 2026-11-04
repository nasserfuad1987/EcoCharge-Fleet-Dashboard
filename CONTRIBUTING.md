# GitHub Collaboration

**Project:** EcoCharge Fleet Dashboard  
**Course Team 4:** Hamdan Mohammad Saeed Bin Salmin Albedwawi; Nasser Fuad Abdulla Ahmad Anwahi; Sultan Ibrahim Mohamad Allanjawi

GitHub provides the source-code history for this software engineering project. The repository includes the original fleet overview and calculator feature branches, their pull requests, and the subsequent improvements to application security, modularity, testing, and documentation.

## Development approach

The team organized changes through feature branches and pull requests rather than treating the application as a single untracked file. The main development history includes [PR #1 — Fleet Overview](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/1), [PR #2 — Calculator Testing and Documentation](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/2), and [PR #4 — Application Quality Improvements](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/4). All three have been merged into `main`.

The repository uses GitHub Actions to execute tests after code changes. This creates a reproducible record of the implemented behavior and reduces reliance on manual calculation alone.

## Collaborative software engineering

The sprint plan describes responsibilities for coordination, application development, and testing. The three members report developing and managing the repository using the **same shared GitHub account (`nasserfuad1987`)**. This explains why the commits and pull requests appear under one username. The GitHub history records shared-account activity rather than individual authorship; task assignments describe the group's planned distribution of work. The assignment specifies feature branches, merged requests, and meaningful commits as evidence of collaboration.

## Code quality conventions

The application separates fixed fleet records (`fleet.py`), monetary calculations (`calculator.py`), web routes (`app.py`), templates, styles, and tests. The project uses descriptive filenames and commit messages. Tests cover normal charging durations, invalid inputs, and Flask form behavior.

For implementation details, see the [architecture](docs/architecture.md), [code review analysis](docs/code_review.md), and [testing evidence](docs/testing_evidence.md).
