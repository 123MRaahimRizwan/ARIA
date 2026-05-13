# 🤖 ARIA – Agentic Resume Intelligence Analyzer

An intelligent, AI-powered suite of tools designed to help job seekers optimize their resumes, prepare for interviews, and improve their candidacy. ARIA leverages advanced language models, RAG (Retrieval Augmented Generation), and multi-agent systems to provide comprehensive career support.

---

## 🌟 Features

### 📄 **Resume Matcher**
- Match your resume against job descriptions
- Get semantic similarity scores and recommendations
- Identify skill gaps and missing qualifications
- Optimize your resume for specific roles

### 📊 **ATS Checker**
- Analyze Applicant Tracking System compatibility
- Check formatting, keywords, and structure
- Get actionable feedback to improve ATS scores
- Ensure your resume passes automated screening

### 💬 **Interview Prep Chatbot**
- AI-powered interview preparation with RAG
- Access knowledge base on AI Ethics, Blockchain, Cloud Computing, and more
- Get instant answers to interview questions
- Practice with domain-specific topic experts
- Real-time learning and personalized feedback

### 🎤 **Mock Interview Analyzer**
- AI-powered speech and response analysis
- **Clarity Analysis**: Evaluate speech clarity, filler words, and sentence structure
- **Confidence Assessment**: Measure volume, pitch variation, and speech rate
- **Sentiment Analysis**: Determine emotional tone and delivery confidence
- **Keyword Matching**: Advanced semantic matching with ideal answers
- **Fluency Evaluation**: Assess coherence and speech flow
- Generate detailed performance reports with actionable insights

---

## 🛠️ Tech Stack

### Core Framework
- **Streamlit** - Interactive web UI
- **LangChain** - LLM orchestration and RAG pipelines
- **Groq LLM** (llama-3.1-8b-instant) - Fast LLM inference
- **OpenAI** - Advanced language model capabilities

### AI & Machine Learning
- **Sentence Transformers** - Semantic embeddings
- **FAISS** - Efficient vector search and retrieval
- **ChromaDB** - Vector database for embeddings
- **Rank-BM25** - Hybrid search capabilities

### Data & Processing
- **PyPDF & PyMuPDF** - PDF text extraction
- **NLTK & spaCy** - NLP preprocessing
- **scikit-learn** - Machine learning utilities
- **Prefect** - Workflow orchestration

### Document Generation
- **reportlab** & **fpdf2** - PDF report generation

### Testing
- **pytest** - Unit and integration tests

---

## 📁 Project Structure

```
ARIA/
├── agents/                          # Agent-based components
│   ├── advisor_agent.py             # Career advisor agent
│   ├── ats_agent.py                 # ATS analysis agent
│   ├── embedding_agent.py           # Embedding generation agent
│   ├── ingestion_agent.py           # Data ingestion agent
│   ├── pdf_generator_agent.py       # Report generation agent
│   └── report_generator_agent.py    # Analysis report generation
├── core/                            # Core functionality
│   ├── ats.py                       # ATS analyzer
│   ├── embedding.py                 # Embedding generation
│   ├── llm_interface.py             # LLM interactions
│   ├── pdf_generator.py             # PDF report generation
│   ├── report_generator.py          # Report generation logic
│   ├── utils.py                     # Utility functions
│   └── data/output/                 # Generated outputs
├── ui/                              # Streamlit UI modules
│   ├── resume_match_ui.py           # Resume matcher interface
│   ├── ats_checker_ui.py            # ATS checker interface
│   ├── interview_prep_ui.py         # Interview prep chatbot
│   └── mock_interview_ui.py         # Mock interview interface
├── rag_core/                        # RAG pipeline components
│   ├── rag_loader.py                # RAG document loader
│   ├── retriever.py                 # Vector retrieval
│   ├── vectorstore_builder.py       # Vector store construction
│   ├── create_mock_data.py          # Sample data generation
│   └── interview_prep_kb/           # Knowledge base (JSON files)
├── mock_interview/                  # Mock interview module
│   └── core/
│       ├── audio_processor.py       # Audio processing
│       └── interview_analyzer.py    # Interview analysis
├── workflows/                       # Pipeline definitions
│   └── resume_match_pipeline.py     # Resume matching workflow
├── config/                          # Configuration files
│   ├── logging_config.yaml          # Logging configuration
│   ├── prompts.yaml                 # LLM prompts
│   └── settings.yaml                # Application settings
├── data/                            # Data directories
│   ├── raw/                         # Raw input data
│   ├── output/                      # Generated outputs
│   ├── embeddings/                  # Vector stores
│   └── fonts/                       # Font files
├── main.py                          # Main Streamlit application
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- API keys for:
  - **Groq** (for LLM inference)
  - **OpenAI** (optional, for advanced models)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ARIA
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # or
   source venv/bin/activate      # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key  # Optional
   ```

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

---

## 💡 Usage Guide

### Resume Matcher
1. Navigate to the **📄 Resume Matcher** tab
2. Upload your resume (PDF or text)
3. Enter the job description
4. View matching score and recommendations
5. Get suggestions for improving your resume

### ATS Checker
1. Go to the **📊 ATS Checker** tab
2. Upload your resume
3. Optionally provide a job description
4. Review ATS compatibility score
5. Check detailed feedback and formatting suggestions

### Interview Prep Chatbot
1. Navigate to the **💬 Interview Prep Chatbot** tab
2. Ask questions about interview topics
3. Access knowledge base on:
   - AI Ethics & Governance
   - Blockchain & Web3
   - Cloud Computing (AWS, Azure, GCP)
   - And 15+ other domains
4. Get tailored answers with follow-up resources

### Mock Interview Analyzer
1. Go to the **🎤 Mock Interview Analyzer** tab
2. Record or upload your interview response
3. Answer interview questions
4. View detailed analysis:
   - Speech clarity and fluency
   - Confidence metrics
   - Sentiment analysis
   - Keyword matching
5. Download comprehensive performance reports

---

## 🔧 Configuration

### Logging Configuration
Edit `config/logging_config.yaml` to customize logging behavior:
```yaml
version: 1
disable_existing_loggers: false
# ... logger configurations
```

### Application Settings
Configure general application behavior in `config/settings.yaml`:
```yaml
# API endpoints, model parameters, thresholds, etc.
```

### LLM Prompts
Customize prompts for various agents in `config/prompts.yaml`:
```yaml
resume_analysis_prompt: "..."
interview_prep_prompt: "..."
# ... other prompts
```

---

## 🧠 Knowledge Base

The project includes a comprehensive knowledge base covering:

- **AI Ethics** (10 topics): Accountability, Governance, Bias & Fairness, etc.
- **Blockchain** (10 topics): Security, Smart Contracts, DeFi, NFTs, etc.
- **Cloud Computing** (9+ topics): AWS, Azure, GCP, Serverless, etc.
- **Data Science**: Machine Learning, Statistics, Feature Engineering, etc.
- **DevOps & Infrastructure**: CI/CD, Kubernetes, Docker, etc.
- **Web Development**: Frontend, Backend, APIs, Frameworks, etc.
- **Cybersecurity**: Cryptography, Network Security, etc.
- **And 10+ other domains**

Access through the Interview Prep Chatbot or by extending RAG pipelines.

---

## 📊 Workflows

### Resume Match Pipeline
Run the complete resume matching workflow:
```bash
python workflows/resume_match_pipeline.py --resume <path> --jd <path>
```

### Mock Interview Analysis
Run mock interview analysis:
```bash
python run_mock_interview.py
```

---

## 🧪 Testing

Run the test suite:
```bash
pytest test_mock_interview.py -v
```

Or with demo data:
```bash
python demo_mock_interview.py
```

---

## 🤝 Architecture

### Multi-Agent System
- **Ingestion Agent**: Loads and preprocesses documents
- **Embedding Agent**: Generates vector embeddings
- **ATS Agent**: Analyzes ATS compatibility
- **Advisor Agent**: Provides career recommendations
- **Report Generator Agent**: Creates detailed reports
- **PDF Generator Agent**: Generates formatted PDF outputs

### RAG Pipeline
- **Document Loading**: Ingest resumes, job descriptions, KB
- **Vector Embedding**: Convert documents to dense vectors
- **Retrieval**: Find relevant documents for queries
- **Generation**: Use LLM to synthesize answers with context

### Streamlit Interface
- Multi-tab interface for different modules
- Real-time processing and feedback
- Interactive visualizations and metrics
- File upload and download support

---

## 📈 Performance Metrics

- **Response Time**: < 5 seconds for most queries
- **ATS Score Accuracy**: Trained on industry standards
- **Interview Analysis**: Real-time audio processing
- **Vector Search**: Sub-100ms retrieval with FAISS

---

## 🐛 Troubleshooting

### API Key Issues
- Ensure `.env` file exists in project root
- Verify API keys are correctly set: `GROQ_API_KEY`, `OPENAI_API_KEY`
- Check API key permissions and quota

### Import Errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`
- Verify Python path includes project root

### PDF Processing Issues
- Check PDF file is not corrupted
- Ensure sufficient disk space for embeddings
- Verify PyMuPDF wheel is installed: `pip install PyMuPDF==1.24.4`

### Streamlit Port Already in Use
```bash
streamlit run main.py --server.port 8502
```

---

## 📝 Contributing

To contribute to ARIA:
1. Create a feature branch
2. Make your changes
3. Add tests for new functionality
4. Submit a pull request

---

## 📄 License

This project is provided as-is for educational and professional use.

---

## 📧 Support

For issues, questions, or feature requests, please:
1. Check existing documentation
2. Review configuration files
3. Run tests to diagnose issues
4. Contact the development team

---

## 🎯 Roadmap

- [ ] Advanced resume formatting templates
- [ ] Real-time salary negotiation advisor
- [ ] Video interview analysis
- [ ] Company culture fit analysis
- [ ] LinkedIn profile optimization
- [ ] Interview scheduling integration
- [ ] Multi-language support
- [ ] Mobile app development

---

**ARIA** – Your Intelligent Career Intelligence Platform
