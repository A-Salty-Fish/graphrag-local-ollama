# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Fine-tuning prompts for entity extraction, entity summarization, and community report summarization."""

from .community_report_summarization import COMMUNITY_REPORT_SUMMARIZATION_PROMPT_ZH
from .entity_extraction import (
    EXAMPLE_EXTRACTION_TEMPLATE,
    GRAPH_EXTRACTION_JSON_PROMPT_ZH,
    GRAPH_EXTRACTION_PROMPT_ZH,
    UNTYPED_EXAMPLE_EXTRACTION_TEMPLATE_ZH,
    UNTYPED_GRAPH_EXTRACTION_PROMPT_ZH,
)
from .entity_summarization import ENTITY_SUMMARIZATION_PROMPT_ZH

__all__ = [
    "COMMUNITY_REPORT_SUMMARIZATION_PROMPT_ZH",
    "ENTITY_SUMMARIZATION_PROMPT_ZH",
    "EXAMPLE_EXTRACTION_TEMPLATE",
    "GRAPH_EXTRACTION_JSON_PROMPT_ZH",
    "GRAPH_EXTRACTION_PROMPT_ZH",
    "UNTYPED_EXAMPLE_EXTRACTION_TEMPLATE_ZH",
    "UNTYPED_GRAPH_EXTRACTION_PROMPT_ZH",
]
