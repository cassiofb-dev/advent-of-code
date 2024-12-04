<h1 align="center">
  Advent of Code
</h1>

<h4 align="center">Benchmark and solutions for AOC</h4>

<p align="center">
  <a href="#about">About</a> •
  <a href="#usage">Usage</a> •
  <a href="#benchmarks">Benchmarks</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## About

This repository contains benchmarks and solutions for the [Advent of Code](https://adventofcode.com) problems.
The solutions are written in different languages and the benchmarks are generated with [Hyperfine](https://github.com/sharkdp/hyperfine).

## Usage

Run in your terminal ``docker compose up -d``. You can check the results on the file ``run_solutions.txt`` created on root directory or inside the programs directory with a txt file created for each program.

To use it without docker make sure you have installed the programs in the section [credits](#credits) and run ``python run_solutions.py``.

A benchmark can be produced with ``python run_solutions.py benchmark`` the result file will be ``run_solutions.md`` in root directory.

## Benchmarks

The benchmarks bellow were generated with [Hyperfine](https://github.com/sharkdp/hyperfine) in 100 warmups and 100 runs:

| Command | Mean [ms] | Min [ms] | Max [ms] | Relative |
|:---|---:|---:|---:|---:|
| `python /advent-of-code/editions/2024/02/part_1.py` | 17.6 ± 0.4 | 17.0 | 18.6 | 8.99 ± 0.48 |
| `/advent-of-code/editions/2024/02/part_2.c.bin` | 2.0 ± 0.1 | 1.7 | 2.4 | 1.00 |
| `python /advent-of-code/editions/2024/02/part_2.py` | 23.1 ± 0.3 | 22.6 | 24.9 | 11.79 ± 0.60 |
| `python /advent-of-code/editions/2024/01/part_1.py` | 16.5 ± 0.2 | 16.2 | 17.0 | 8.41 ± 0.42 |
| `python /advent-of-code/editions/2024/01/part_2.py` | 24.4 ± 2.2 | 23.4 | 33.7 | 12.46 ± 1.26 |

## Credits

Thanks for these awesome open source projects bellow:

- [Hyperfine](https://github.com/sharkdp/hyperfine)
- [Docker](https://github.com/docker)
- [NodeJS](https://github.com/nodejs)
- [Python](https://github.com/python)
- [Java](https://github.com/openjdk/jdk)
- [Rust](https://github.com/rust-lang/rust)
- [GCC](https://github.com/gcc-mirror/gcc)

## License

MIT

---

> [Website](https://cassiofernando.com) &nbsp;&middot;&nbsp;
> GitHub [@cassiofb-dev](https://github.com/cassiofb-dev) &nbsp;&middot;&nbsp;
> Twitter [@cassiofb_dev](https://twitter.com/cassiofb_dev)
