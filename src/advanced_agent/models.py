from typing import List, Optional, Dict, Any
from pydantic import BaseModel

#BaseModel is the foundation of Pydantic.
class CompanyAnalysis(BaseModel):

    pricing_model: str  # Free, Premium, Paid, Enterprise, Unknown
    is_open_source: Optional[bool] = None
    tech_stack: List[str] = []
    description: str = ""
    api_available: Optional[bool] = None   #The '= None' means the default value is None.
    language_support: List[str] = []
    integration_capabilities: List[str] = []


class CompanyInfo(BaseModel):
    # LLMs normally return unstructured text.
    # but this class will tell the llm to Create a structured data model called CompanyInfo,
    # and Pydantic should validate the data going into it.
    name: str
    description: str
    website: str
    pricing_model: Optional[str] = None
    is_open_source: Optional[bool] = None
    tech_stack: List[str] = []
    competitors: List[str] = []
    # Developer-specific fields
    api_available: Optional[bool] = None
    language_support: List[str] = []
    integration_capabilities: List[str] = []
    developer_experience_rating: Optional[str] = None  # Poor, Good, Excellent


class ResearchState(BaseModel):
    #ResearchState is the agent's notebook.
    #As the LangGraph agent works, it needs somewhere to keep information.

    query: str
    extracted_tools: List[str] = []  # Tools extracted from articles
    companies: List[CompanyInfo] = []
    search_results: List[Dict[str, Any]] = []
    analysis: Optional[str] = None