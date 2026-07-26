"""Scientific Question Backtesting Benchmark.

A model-agnostic protocol for evaluating whether AI-generated scientific
questions anticipate future scientific progress. Questions are frozen
against literature available before a historical cutoff and evaluated
against a temporally isolated future corpus.

Pipeline: import questions -> temporal isolation -> future-evidence
retrieval -> outcome judging -> metrics -> benchmark report.
"""

__version__ = "1.0.0"
PROTOCOL_VERSION = "1.0"
