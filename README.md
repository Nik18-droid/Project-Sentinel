# Project Sentinel 🎯

### AI-Augmented Customer Churn Analysis Platform

---

## 📋 Table of Contents

- [Overview](#overview)
- [The Problem](#the-problem)
- [The Solution](#the-solution)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Key Features](#key-features)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Insights & Results](#key-insights--results)
- [Skills Demonstrated](#skills-demonstrated)
- [Future Enhancements](#future-enhancements)
- [Documentation](#documentation)
- [Author](#author)

---

## 🎯 Overview

Project Sentinel is a comprehensive, AI-augmented customer churn analysis platform that transforms traditional manual analysis (2+ hours) into conversational, real-time insights (30 seconds). Built to demonstrate modern Business Analyst capabilities, this project combines traditional analytical rigor (SQL, Power BI) with emerging AI technologies (Python, OpenAI API) to solve a critical SaaS business problem.

**What makes this different:** Most BA portfolios show disconnected SQL queries and static dashboards. Project Sentinel delivers a complete, integrated platform where stakeholders can explore churn data through natural conversation with an AI assistant named "Stuart."

---

## 🔍 The Problem

### Business Context

Traditional customer churn analysis faces three critical challenges:

1. **Time-Intensive**: Manual analysis takes 2-3 hours per cycle (SQL queries → Excel charts → PowerPoint → stakeholder email)
2. **Static Insights**: Reports are outdated by the time they arrive; follow-up questions restart the entire cycle
3. **Non-Scalable**: Analysis frequency limited by analyst availability; can't scale without hiring

### Business Impact

For a mid-sized SaaS company (ProjectFlow) with 5,000 customers:
- **8.5% churn rate** (425 customers churning annually)
- **₹20.6 lakhs monthly recurring revenue at risk**
- **₹2.47 crores annual revenue exposure**
- Executive team lacks real-time visibility into churn patterns

---

## 💡 The Solution

### Project Sentinel: 5-Component Architecture

Project Sentinel reimagines churn analysis as an AI-augmented, self-service platform:

**1. Data Foundation** - Professional-quality synthetic dataset (5,000 customers with realistic churn patterns)  
**2. SQL Analysis Engine** - 10 analytical queries answering specific business questions  
**3. Power BI Dashboard** - 3-page interactive visualization for executives and analysts  
**4. AI Insights Engine (Stuart)** - Conversational interface enabling natural language exploration  
**5. Business Documentation** - Complete technical and business documentation for presentations

### Value Delivered

✅ **99% time reduction** (2 hours → 30 seconds per analysis)  
✅ **Real-time insights** enabling faster intervention  
✅ **Democratized access** for non-technical stakeholders  
✅ **₹7.7 lakhs projected annual savings** from improved retention

---

## 🛠️ Tech Stack

### Data & Analysis
- **Python 3.9+** - Data generation, API integration, web framework
- **MySQL 8.0** - Data storage and analytical queries
- **Pandas 2.0.3** - Data manipulation and statistical analysis
- **NumPy** - Numerical operations and distributions

### Visualization & UI
- **Power BI Desktop** - Interactive dashboard with DAX measures
- **Streamlit 1.28.0** - Web application framework
- **Plotly 5.17.0** - Interactive charts (gauge, bar, comparison)

### AI Integration
- **OpenAI API (gpt-3.5-turbo)** - Natural language processing
- **Prompt Engineering** - Custom system prompts for conversational behavior

### Supporting Libraries
- **Faker** - Realistic synthetic data generation
- **python-dotenv** - Environment variable management

---

## 🏗️ Architecture

### System Overview

```
┌──────────────────────────────────────────────────────────────┐
│                    PROJECT SENTINEL                          │
│            End-to-End Analytics Platform                     │
└──────────────────────────────────────────────────────────────┘
                            ↓
        ┌───────────────────┴───────────────────┐
        │                                       │
   ┌────▼─────┐                         ┌──────▼─────┐
   │Component 1│                         │Component 5 │
   │   DATA    │                         │    DOCS    │
   │Foundation │                         │  Business  │
   └────┬─────┘                          │  Context   │
        │                                 └────────────┘
        │ (CSV Export)
        ↓
   ┌────▼─────┐        (Results)        ┌────────────┐
   │Component 2│ ──────────────────────→│Component 3 │
   │    SQL    │                         │  Power BI  │
   │  Analysis │                         │ Dashboard  │
   └────┬─────┘                          └────────────┘
        │
        │ (CSV Results)
        ↓
   ┌────▼─────┐
   │Component 4│
   │     AI    │
   │  Insights │
   │  (Stuart) │
   └───────────┘
```

### Data Flow

1. **Data Generation** → Custom Python script creates 5,000 customer records with realistic business logic
2. **SQL Analysis** → 10 queries extract patterns, calculate metrics, score risk
3. **Power BI Visualization** → 3-page dashboard displays insights interactively
4. **AI Interface** → Stuart enables conversational exploration of churn data
5. **Documentation** → Complete technical and business materials for presentations

---

## ✨ Key Features

### 🤖 Stuart: The Conversational AI Assistant

- **Natural Language Queries**: Ask questions like "Why are customers churning?" or "Show me high-risk customers"
- **Dynamic Data Calculation**: Metrics calculated on-the-fly using Pandas (no pre-computed reports)
- **Intelligent Response**: Detects query intent and responds with text or data tables appropriately
- **Conversational Tone**: Engineered to feel like talking to a colleague, not querying a database
- **Conversation History**: Maintains context across multiple questions

### 📊 Power BI Dashboard

- **3-Page Architecture**: Overview, Driver Analysis, Action Intelligence
- **Custom DAX Measures**: Churn rate, revenue at risk, risk multipliers
- **Interactive Filtering**: Cross-highlighting, drill-down, segment slicers
- **Executive-Friendly**: Visual storytelling with gauge charts, comparison bars, risk tables

### 🔍 SQL Analysis Framework

- **10 Strategic Queries**: Each solving a specific business question
- **Risk Scoring Algorithm**: Multi-factor weighted model (contract, onboarding, engagement, support, usage)
- **Segment Analysis**: Contract type, pricing tier, engagement levels, revenue brackets
- **Revenue Quantification**: Calculates financial impact by segment

### 📈 Professional Data Quality

- **Realistic Patterns**: Custom generator ensures business logic correlations
- **Statistical Distributions**: Normal, Poisson distributions for natural variation
- **Quality Controls**: Validated 8.5% churn rate, 3.3x and 2.5x risk multipliers
- **Reproducible**: Seeded random generation for consistent results

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- MySQL 8.0 (for SQL component)
- Power BI Desktop (for dashboard component)
- OpenAI API key (for Stuart component)

### Step 1: Clone Repository

```bash
git clone https://github.com/Nik18-droid/project-sentinel.git
cd project-sentinel
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
streamlit==1.28.0
pandas==2.0.3
plotly==5.17.0
openai==1.3.0
numpy==1.24.3
faker==19.6.2
python-dotenv==1.0.0
```

### Step 4: Set Environment Variables

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

**Get your OpenAI API key:**
1. Sign up at [OpenAI Platform](https://platform.openai.com/)
2. Navigate to API keys section
3. Create new secret key
4. Copy and paste into `.env` file

### Step 5: Generate Data (Optional)

```bash
python data_generator.py
```

This creates `customer_data.csv` with 5,000 customer records.

**Note:** Pre-generated dataset included in repository for immediate use.

### Step 6: Run Stuart Interface

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

---

## 💻 Usage

### Example Queries for Stuart

**Basic Analytics:**
```
"What's the overall churn rate?"
"How much revenue is at risk?"
"How many customers do we have?"
```

**Comparative Analysis:**
```
"Compare monthly vs annual contract churn"
"What's the difference between complete and incomplete onboarding?"
"Show me engagement score impact on churn"
```

**Risk Identification:**
```
"Show me the 10 highest-risk customers"
"Which customers should we focus on?"
"Who is most likely to churn?"
```

**Strategic Questions:**
```
"Why are customers churning?"
"What should we do about this?"
"What are the main churn drivers?"
```

### Stuart's Response Types

**Conversational Answer:**
```
User: "Why are customers churning?"

Stuart: "Looking at the data, monthly contracts are your biggest risk 
factor - they churn at 15.2% compared to just 4.6% for annual contracts. 
That's a 3.3x difference. The incomplete onboarding group is also 
concerning, with churn rates 2.5x higher than those who completed 
onboarding. Combined, these two factors account for about ₹15.2 lakhs 
of the ₹20.6 lakhs total revenue at risk."
```

**Data Table Display:**
```
User: "Show me high-risk customers"

Stuart: "Here are the top 10 customers most likely to churn, 
sorted by risk score and revenue impact:"

[Displays interactive table with customer_id, contract_type, 
pricing_tier, monthly_revenue, risk_score]
```

---

## 📁 Project Structure

```
project-sentinel/
│
├── data/
│   ├── customer_data.csv                 # Generated dataset (5,000 records)
│   └── data_generator.py                 # Custom data generation script
│
├── sql/
│   ├── queries.sql                       # All 10 analytical queries
│   └── schema.sql                        # MySQL database schema
│
├── powerbi/
│   └── sentinel_dashboard.pbix           # Power BI dashboard file
│
├── stuart/
│   ├── app.py                            # Main Streamlit application
│   ├── requirements.txt                  # Python dependencies
│   └── .env.example                      # Environment variable template
│
├── documentation/
│   ├── 01_Executive_Summary.md           # Business value overview
│   ├── 02_Project_Journey.md             # Development story
│   ├── 03_Technical_Architecture.md      # Implementation details
│   ├── 04_Skills_Demonstration_Matrix.md # Competency mapping
│   ├── 05_Interview_Script.md            # Presentation guide
│   └── Study_Notes_Final.md              # 3-page quick reference
│
├── README.md                             # This file
└── LICENSE                               # MIT License
```

---

## 📈 Key Insights & Results

### Business Insights Discovered

#### 1. Contract Type Risk (Primary Driver)
- **Monthly contracts:** 15.2% churn rate
- **Annual contracts:** 4.6% churn rate
- **Risk multiplier:** 3.3x
- **Revenue impact:** ₹8.4 lakhs MRR at risk

#### 2. Onboarding Impact (Secondary Driver)
- **Incomplete onboarding:** 15.48% churn rate
- **Complete onboarding:** 6.12% churn rate
- **Risk multiplier:** 2.5x
- **Revenue impact:** ₹6.8 lakhs MRR at risk

#### 3. Engagement Correlation (Tertiary Driver)
- **Low engagement (<50):** 50% higher churn probability
- **High engagement (60+):** Baseline churn risk
- **Revenue impact:** ₹5.4 lakhs MRR at risk

### Quantified Business Value

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Analysis Time** | 2 hours | 30 seconds | 99% reduction |
| **Data Refresh** | Manual (days) | Real-time | Immediate |
| **Stakeholder Access** | Analyst-gated | Self-service | Democratized |
| **Churn Rate** | 8.5% | 6.3% (projected) | 2.2% reduction |
| **Revenue Protected** | N/A | ₹7.7 lakhs/year | ROI: Immediate |

### Actionable Recommendations

1. **Fix Onboarding Process**
   - Implement mandatory completion checkpoints
   - Follow-up calls for incomplete onboarding
   - Projected impact: ₹6.8L MRR protection

2. **Convert Monthly to Annual**
   - Offer 2-month discount for contract upgrades
   - Target high-value monthly customers first
   - Projected impact: ₹8.4L MRR protection

3. **Proactive Risk Intervention**
   - Weekly outreach to top 100 high-risk customers
   - Engagement score monitoring and alerts
   - Projected impact: 2.2% overall churn reduction

---

## 🎓 Skills Demonstrated

### Technical Skills

**Data Analysis & Databases**
- Advanced SQL (complex queries, joins, aggregations, risk scoring)
- MySQL database design and optimization
- Statistical analysis and data modeling

**Data Visualization**
- Power BI dashboard development
- Custom DAX measure creation
- Interactive visualization design

**Programming & Development**
- Python (Pandas, NumPy, Streamlit, Plotly)
- API integration (OpenAI)
- Web application development
- Error handling and data validation

**AI & Machine Learning**
- Prompt engineering for conversational AI
- Natural language processing integration
- AI-augmented analytics architecture

### Business Analysis Skills

**Problem-Solving**
- Business problem validation
- Root cause analysis
- Solution architecture design

**Data-Driven Decision Making**
- Metric definition and calculation
- Segment analysis and comparison
- ROI calculation and business case development

**Stakeholder Communication**
- Multi-audience documentation
- Executive presentations
- Technical writing

**Process Improvement**
- Workflow automation (99% efficiency gain)
- Scalability design
- Quality assurance

### Project Management

**Planning & Execution**
- 4-day sprint delivery
- Component-based architecture
- Milestone tracking

**Quality Control**
- Iterative development
- Testing and validation
- Production-ready standards

**Adaptability**
- Rapid skill acquisition (Streamlit, OpenAI API)
- Mid-project pivoting (static → conversational)
- Resourcefulness in problem-solving

---

## 🔮 Future Enhancements

### Phase 1: Advanced Analytics (Weeks 1-2)
- [ ] Churn prediction model (Random Forest/XGBoost)
- [ ] Customer lifetime value (LTV) calculation
- [ ] Cohort analysis by signup month
- [ ] Survival analysis curves

### Phase 2: Real-Time Monitoring (Weeks 3-4)
- [ ] Streaming data pipeline
- [ ] Real-time churn alerts via email/Slack
- [ ] Dashboard auto-refresh every 15 minutes
- [ ] Anomaly detection for sudden churn spikes

### Phase 3: Production Deployment (Weeks 5-6)
- [ ] PostgreSQL migration (from CSV)
- [ ] Redis caching layer
- [ ] OAuth 2.0 authentication
- [ ] Docker containerization
- [ ] Cloud deployment (AWS/Azure)

### Phase 4: Enhanced AI Capabilities (Weeks 7-8)
- [ ] Multi-turn conversation memory
- [ ] Sentiment analysis on support tickets
- [ ] Automated intervention recommendations
- [ ] A/B testing framework for retention strategies

---

## 📚 Documentation

Complete documentation available in `/documentation/` directory:

1. **[Executive Summary](documentation/01_Executive_Summary.md)** - Business value overview for non-technical stakeholders
2. **[Project Journey](documentation/02_Project_Journey.md)** - Development story with challenges and decisions
3. **[Technical Architecture](documentation/03_Technical_Architecture.md)** - Complete implementation details with code
4. **[Skills Demonstration Matrix](documentation/04_Skills_Demonstration_Matrix.md)** - Competency mapping for interviews
5. **[Interview Script](documentation/05_Interview_Script.md)** - Presentation guide and Q&A preparation
6. **[Study Notes](documentation/Study_Notes_Final.md)** - 3-page comprehensive quick reference

---

## 👨‍💻 Author

**Nikhil Sharma**  
Junior Business Analyst | AI-Augmented Analytics Specialist

- **LinkedIn:** [linkedin.com/in/nikhilsharma8215](https://linkedin.com/in/nikhilsharma8215)
- **GitHub:** [github.com/Nik18-droid](https://github.com/Nik18-droid)
- **Email:** Nikhil.sharma369@outlook.com
- **Location:** New Delhi, India

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **OpenAI** for the GPT-3.5-turbo API enabling conversational analytics
- **Streamlit** for the intuitive web framework
- **Power BI** for robust visualization capabilities
- **Stack Overflow & AI Communities** for technical problem-solving support

---

## 📞 Contact & Feedback

**Questions about the project?** Feel free to:
- Open an issue in this repository
- Connect with me on [LinkedIn](https://linkedin.com/in/nikhilsharma8215)
- Email me at Nikhil.sharma369@outlook.com

**Looking to collaborate or hire?** I'm actively seeking Business Analyst roles at product companies (Uber, Zomato, Swiggy, etc.) where I can leverage both traditional analytical skills and modern AI capabilities.

---

<div align="center">

**⭐ If you find this project interesting, please consider starring it! ⭐**

**Built with 💡 strategic thinking, 💻 technical execution, and ☕ lots of coffee**

</div>

---

*Last Updated: October 30, 2025*  
*Project Status: Complete & Interview-Ready*  
*Development Time: 4 days (38 active hours)*
