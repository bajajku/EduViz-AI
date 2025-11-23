# EduViz AI: Animated Curriculum Assistant

## 🎯 Aligned with UN Sustainable Development Goal 4
### **Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all**

EduViz AI directly addresses Goal 4 by democratizing access to high-quality educational content through AI-powered video generation. Our platform transforms static educational materials into engaging, animated videos, making complex concepts accessible to learners worldwide regardless of their background or resources.

---

## 💡 Inspiration

Traditional educational content creation is time-consuming, expensive, and requires specialized skills in animation and video production. Many educators and institutions struggle to create engaging visual content that helps students understand complex concepts, especially in STEM fields. 

We were inspired by the need to:
- **Democratize educational content creation**: Enable anyone to create professional-quality educational animations without animation expertise
- **Bridge the accessibility gap**: Make learning materials more engaging and accessible to diverse learners
- **Accelerate curriculum development**: Help educators quickly transform textbooks, PDFs, and notes into animated video content
- **Support lifelong learning**: Enable self-learners to create personalized educational content from any source material

The vision is to make high-quality educational animations as easy to create as writing a document, thereby supporting inclusive and equitable quality education for all.

---

## 🚀 What it does

EduViz AI is an intelligent system that automatically converts educational documents (PDFs, text, course materials) into professional animated videos using Manim (Mathematical Animation Engine). The platform:

### Core Capabilities:

1. **Intelligent Document Processing**
   - Extracts and analyzes content from PDFs and text inputs
   - Performs semantic analysis to understand educational concepts
   - Identifies mathematical formulas, diagrams, and key concepts

2. **Multi-Scene Video Generation**
   - Automatically chunks large documents into logical, digestible scenes
   - Creates smooth transitions between scenes
   - Generates complete multi-part educational videos

3. **AI-Powered Content Analysis**
   - Uses Google Gemini AI to understand content structure and context
   - Identifies optimal visualization strategies for different content types
   - Determines appropriate animations, timing, and visual hierarchy

4. **Automated Code Generation**
   - Generates production-ready Manim Python code
   - Handles complex animations, mathematical notation, and visual elements
   - Ensures proper formatting, timing, and visual consistency

5. **Interactive Web Interface**
   - User-friendly Gradio-based frontend
   - Real-time video generation and preview
   - Detailed analytics and statistics on generated content

### Key Features:
- ✅ **PDF Processing**: Upload PDF documents and automatically extract content
- ✅ **Text Input**: Direct text input for quick video generation
- ✅ **Multi-Scene Support**: Automatically splits large content into multiple coordinated scenes
- ✅ **Mathematical Content**: Special handling for formulas, equations, and mathematical concepts
- ✅ **Quality Control**: Automatic text sizing, positioning, and overflow prevention
- ✅ **Video Statistics**: Comprehensive analytics on scene duration, objects, animations
- ✅ **Export Options**: Download generated code and videos in multiple quality settings

---

## 🛠️ How we built it

### Architecture Overview

EduViz AI is built using a modular, pipeline-based architecture that processes educational content through multiple stages:

```
Input (PDF/Text) → Content Analysis → Scene Structuring → Code Generation → Video Rendering
```

### Technology Stack

**Backend & AI:**
- **Python 3.x**: Core language
- **Google Gemini AI (gemini-2.5-pro/flash)**: Content analysis and code generation
- **LangChain**: LLM integration and management
- **Manim Community Edition**: Mathematical animation engine

**Data Processing:**
- **PyPDF2/pdfplumber**: PDF text extraction
- **JSON**: Structured data representation
- **Custom parsing modules**: Content structure analysis

**Frontend:**
- **Gradio**: Interactive web interface
- **HTML/CSS**: Custom styling and UI components

**Video Processing:**
- **Manim**: Video rendering engine
- **FFmpeg**: Video encoding (via Manim)

### System Components

#### 1. **Data Processing Pipeline** (`data_processing/`)
   - **Input Processor**: Extracts and structures raw content from PDFs/text
   - **Multi-Scene Processor**: Intelligently chunks large documents into logical sections
   - **Scene Parser**: Converts structured data into animation-ready formats
   - **Document Chunker**: Uses AI to identify optimal breakpoints in content

#### 2. **AI & LLM Integration** (`models/`)
   - **LLM Factory**: Unified interface for multiple AI providers
   - **Google Gemini Integration**: Content understanding and code generation
   - **Temperature Control**: Optimized for consistent, reliable outputs

#### 3. **Code Generation** (`code_generation/`)
   - **Manim Code Generator**: Converts scene structures into executable Python code
   - **Code Validation**: Syntax checking and error correction
   - **Modern API Support**: Ensures compatibility with latest Manim versions
   - **Text Overflow Prevention**: Automatic sizing and positioning

#### 4. **Execution Engine** (`execution/`)
   - **Manim Executor**: Runs generated code and renders videos
   - **Quality Management**: Multiple quality presets (480p, 720p, 1080p)
   - **Error Handling**: Graceful failure recovery

#### 5. **Frontend Interface** (`frontend/`)
   - **Gradio App**: User-friendly web interface
   - **Real-time Processing**: Live status updates and progress tracking
   - **Video Preview**: In-browser video playback
   - **Statistics Dashboard**: Detailed analytics on generated content

### Data Analysis & Intelligence

The system employs sophisticated data analysis techniques:

1. **Content Analysis**
   - Semantic understanding of educational content
   - Identification of key concepts, formulas, and visual elements
   - Optimal scene duration and pacing calculations

2. **Document Chunking Intelligence**
   - AI-powered logical section identification
   - Priority-based scene ordering
   - Content type classification (introduction, formula, concept, example, summary)

3. **Statistical Analysis**
   - Scene duration optimization
   - Object and animation counting
   - Content density analysis
   - Video structure metrics

4. **Quality Metrics**
   - Text overflow detection and prevention
   - Positioning optimization
   - Animation timing analysis
   - Visual consistency checks

### Development Process

1. **Research Phase**: Studied Manim capabilities and educational content requirements
2. **Prototype Development**: Built initial single-scene generation pipeline
3. **Multi-Scene Enhancement**: Extended to handle large documents with multiple scenes
4. **AI Integration**: Integrated Google Gemini for intelligent content analysis
5. **Frontend Development**: Created user-friendly Gradio interface
6. **Quality Assurance**: Implemented code validation and error correction
7. **Testing & Refinement**: Tested with various educational content types

---

## 🎯 Challenges we ran into

### Technical Challenges

1. **Code Generation Quality**
   - **Challenge**: LLM-generated code often had syntax errors, deprecated API usage, and formatting issues
   - **Solution**: Implemented comprehensive code validation, cleaning, and modern API migration
   - **Result**: Automatic detection and fixing of common issues (text overflow, deprecated methods, timing errors)

2. **Text Overflow and Positioning**
   - **Challenge**: Generated text frequently overflowed frame boundaries or overlapped
   - **Solution**: Developed intelligent text sizing system with automatic `set_max_width()` application and vertical spacing algorithms
   - **Result**: All text objects are automatically constrained and properly positioned

3. **Multi-Scene Coordination**
   - **Challenge**: Ensuring smooth transitions and logical flow between multiple scenes
   - **Solution**: Implemented intelligent document chunking with AI-powered section identification and priority-based ordering
   - **Result**: Cohesive multi-part videos with natural scene progression

4. **PDF Processing Reliability**
   - **Challenge**: Different PDF formats and structures required robust extraction
   - **Solution**: Implemented fallback mechanisms using multiple PDF libraries (PyPDF2, pdfplumber)
   - **Result**: Reliable text extraction from various PDF formats

5. **Timing and Animation Synchronization**
   - **Challenge**: Complex timing calculations led to negative wait times and animation conflicts
   - **Solution**: Developed conditional timing system with current_time tracking and validation
   - **Result**: Smooth, error-free animation timelines

6. **LLM Response Parsing**
   - **Challenge**: Inconsistent JSON formatting from LLM responses
   - **Solution**: Robust JSON cleaning and parsing with multiple fallback strategies
   - **Result**: Reliable extraction of structured data from AI responses

### Data Analysis Challenges

1. **Content Structure Understanding**
   - **Challenge**: Accurately identifying logical sections and educational concepts
   - **Solution**: Fine-tuned AI prompts with educational context and structured output requirements
   - **Result**: Intelligent content segmentation and scene generation

2. **Optimal Chunking Strategy**
   - **Challenge**: Balancing chunk size with educational coherence
   - **Solution**: AI-powered chunking that considers topic boundaries, formula density, and optimal scene duration
   - **Result**: Natural, educationally-sound scene divisions

3. **Statistical Accuracy**
   - **Challenge**: Tracking and reporting accurate video generation metrics
   - **Solution**: Comprehensive data collection throughout the pipeline with detailed analytics
   - **Result**: Rich statistics on scenes, objects, animations, and timing

---

## 🏆 Accomplishments that we're proud of

### Technical Achievements

1. **End-to-End Automation**
   - Successfully created a fully automated pipeline from document input to video output
   - Zero manual intervention required for standard educational content

2. **Intelligent Content Analysis**
   - Developed sophisticated AI-powered content understanding that identifies:
     - Mathematical formulas and equations
     - Key concepts and learning objectives
     - Optimal visualization strategies
     - Natural content breakpoints

3. **Robust Code Generation**
   - Generated code that is production-ready and follows Manim best practices
   - Automatic error detection and correction
   - Support for complex animations and mathematical notation

4. **Multi-Scene Architecture**
   - Successfully implemented intelligent document chunking
   - Created seamless multi-part video generation
   - Maintained visual and narrative consistency across scenes

5. **User Experience**
   - Built an intuitive web interface that requires no technical knowledge
   - Real-time feedback and progress tracking
   - Comprehensive statistics and analytics

### Data Analysis Achievements

1. **Advanced Content Processing**
   - Intelligent semantic analysis of educational materials
   - Automatic identification of content types and structures
   - Optimal scene duration and pacing calculations

2. **Statistical Insights**
   - Comprehensive video generation metrics
   - Scene-by-scene breakdown with object and animation counts
   - Content density and complexity analysis

3. **Quality Optimization**
   - Automatic detection and prevention of visual issues
   - Text sizing and positioning optimization
   - Animation timing and synchronization analysis

### Impact on Education (SDG 4)

1. **Accessibility**
   - Makes professional-quality educational content creation accessible to all educators
   - Removes barriers of cost and technical expertise

2. **Scalability**
   - Enables rapid creation of educational content at scale
   - Supports curriculum development for diverse subjects

3. **Inclusivity**
   - Helps create content for diverse learning styles
   - Supports multiple languages and educational contexts

4. **Innovation**
   - Pioneers AI-powered educational content generation
   - Demonstrates practical application of AI for social good

---

## 📚 What we learned

### Technical Learnings

1. **LLM Integration Best Practices**
   - Importance of structured prompts and output validation
   - Temperature tuning for different use cases (analysis vs. code generation)
   - Handling inconsistent LLM responses gracefully

2. **Manim Development**
   - Deep understanding of Manim's animation system and API
   - Best practices for text handling, positioning, and animation timing
   - Modern API migration and deprecation management

3. **System Architecture**
   - Benefits of modular, pipeline-based design
   - Importance of error handling and fallback mechanisms
   - Balancing automation with quality control

4. **Data Processing**
   - Effective strategies for document chunking and content analysis
   - Handling various input formats and edge cases
   - Optimizing for both accuracy and performance

### Data Analysis Insights

1. **Content Understanding**
   - Educational content has distinct structural patterns
   - Mathematical content requires specialized handling
   - Visual hierarchy is crucial for effective learning

2. **Optimal Scene Structure**
   - 30-60 second scenes are optimal for educational content
   - Logical topic boundaries improve comprehension
   - Smooth transitions maintain engagement

3. **Quality Metrics**
   - Text overflow is a common issue that requires proactive prevention
   - Proper spacing and sizing significantly impact visual quality
   - Timing synchronization is critical for professional results

### Educational Impact

1. **Content Creation Barriers**
   - Technical barriers significantly limit educational content creation
   - Cost and time constraints prevent many educators from creating visual content
   - AI can effectively bridge these gaps

2. **Learning Effectiveness**
   - Animated content significantly improves concept comprehension
   - Visual representation helps with abstract and mathematical concepts
   - Multi-scene structure supports progressive learning

3. **Accessibility Needs**
   - Diverse learners benefit from different content formats
   - Automated generation enables rapid content creation for various needs
   - Scalability is essential for widespread educational impact

---

## 🔮 What's next for EduViz AI: Animated Curriculum Assistant

### Short-term Enhancements (Next 3-6 months)

1. **Enhanced AI Capabilities**
   - Fine-tuned models specifically for educational content
   - Support for more languages and educational contexts
   - Improved formula and diagram recognition

2. **Advanced Visualizations**
   - Support for more complex diagrams and graphs
   - Interactive elements and annotations
   - Customizable visual styles and themes

3. **User Experience Improvements**
   - Batch processing for multiple documents
   - Template library for common educational content types
   - Enhanced preview and editing capabilities

4. **Performance Optimization**
   - Faster video generation through caching and optimization
   - Parallel scene processing
   - Cloud-based rendering options

### Medium-term Goals (6-12 months)

1. **Collaboration Features**
   - Multi-user support for educational institutions
   - Version control and content sharing
   - Collaborative editing and review workflows

2. **Advanced Analytics**
   - Learning effectiveness metrics
   - Content engagement analysis
   - Personalized content recommendations

3. **Integration Ecosystem**
   - LMS (Learning Management System) integrations
   - API for third-party applications
   - Plugin architecture for extensibility

4. **Accessibility Enhancements**
   - Closed captioning and subtitles
   - Audio narration generation
   - Multi-language support

### Long-term Vision (1+ years)

1. **AI-Powered Personalization**
   - Adaptive content generation based on learner profiles
   - Difficulty level adjustment
   - Personalized learning paths

2. **Community Platform**
   - Content marketplace for educational videos
   - Community-contributed templates and styles
   - Knowledge sharing and best practices

3. **Research & Development**
   - Collaboration with educational researchers
   - Studies on learning effectiveness
   - Continuous improvement based on user feedback

4. **Global Impact**
   - Support for underserved educational communities
   - Partnerships with educational organizations
   - Open-source contributions and community building

### Data Analysis Roadmap

1. **Advanced Analytics Dashboard**
   - Real-time content analysis metrics
   - Predictive quality scoring
   - Optimization recommendations

2. **Machine Learning Enhancements**
   - Content quality prediction models
   - Optimal scene structure learning
   - User preference learning

3. **Research Applications**
   - Educational content effectiveness studies
   - Learning pattern analysis
   - Content optimization research

---

## 📊 Data Analysis Highlights

### Content Processing Analytics

- **Document Analysis**:** Intelligent extraction and understanding of educational content structure
- **Semantic Segmentation**: AI-powered identification of logical sections and topics
- **Content Classification**: Automatic categorization (introduction, formula, concept, example, summary)
- **Complexity Scoring**: Assessment of content difficulty and visualization requirements

### Video Generation Metrics

- **Scene Statistics**: Duration, object count, animation count per scene
- **Timing Analysis**: Optimal pacing calculations and synchronization
- **Quality Metrics**: Text overflow prevention, positioning optimization, visual consistency
- **Performance Tracking**: Generation time, success rates, error patterns

### Educational Impact Analysis

- **Content Accessibility**: Metrics on content creation barriers removed
- **Scalability Metrics**: Volume of content that can be generated
- **Diversity Support**: Analysis of content types and educational contexts supported
- **User Engagement**: Statistics on generated content usage and effectiveness

---

## 🎓 Contributing to SDG 4: Quality Education

EduViz AI directly supports **UN Sustainable Development Goal 4** by:

1. **Democratizing Access**: Making professional educational content creation accessible to all
2. **Reducing Barriers**: Eliminating cost and technical expertise requirements
3. **Enhancing Quality**: Enabling creation of high-quality, engaging educational materials
4. **Supporting Diversity**: Facilitating content creation for diverse learners and contexts
5. **Promoting Lifelong Learning**: Enabling self-learners to create personalized educational content
6. **Scalability**: Supporting rapid content creation at institutional and global scales

Through intelligent data analysis and AI-powered automation, EduViz AI transforms the educational content creation landscape, making quality education more accessible, engaging, and inclusive for learners worldwide.

---

## 📝 Technical Specifications

- **Language**: Python 3.x
- **AI Models**: Google Gemini 2.5 Pro/Flash
- **Animation Engine**: Manim Community Edition
- **Frontend**: Gradio
- **PDF Processing**: PyPDF2, pdfplumber
- **LLM Framework**: LangChain
- **Architecture**: Modular pipeline-based system

---

## 🙏 Acknowledgments

This project represents a significant step toward democratizing educational content creation through AI and data analysis. We're committed to continuing development and contributing to the global goal of inclusive, equitable quality education for all.

---

*Built with ❤️ for education and SDG 4*

