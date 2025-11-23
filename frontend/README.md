# Manim Video Generator - Gradio Frontend

A simple and intuitive web interface for the Manim Video Generation Pipeline.

## Features

🎬 **Easy Video Generation**: Transform documents and text into engaging educational videos  
📄 **Multiple Input Types**: Support for PDF uploads, direct text input, or both  
🎯 **Smart Processing**: Automatic document chunking and multi-scene generation  
📊 **Real-time Statistics**: Detailed video statistics and scene breakdowns  
💾 **Code Export**: Download generated Manim code ready for execution  

## Quick Start

### Prerequisites

1. **Google Gemini API Key**: Get one at [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Python Environment**: Ensure you're using the project's virtual environment

### Running the Frontend

1. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

2. **Launch the frontend:**
   ```bash
   python run_frontend.py
   ```

3. **Open your browser** to the URL shown (typically http://localhost:7860)

## How to Use

### Input Options

- **📄 PDF Upload**: Upload any PDF document for processing
- **📝 Text Input**: Enter text content directly (supports markdown)
- **🎬 Video Title**: Provide a descriptive title for your video
- **📋 Instructions**: Add specific styling or content instructions
- **🔑 API Key**: Provide your Gemini API key (or set `GOOGLE_API_KEY` environment variable)

### Processing

1. Choose your input method (PDF, text, or both)
2. Fill in the video title and any additional instructions
3. Click "🚀 Generate Video Code"
4. Wait for processing to complete

### Output

The interface provides:

- **📊 Status**: Processing status and summary statistics
- **📈 Video Statistics**: Detailed breakdown of scenes, duration, and content
- **📄 Generated Code**: Complete Manim code ready for execution

### Using the Generated Code

1. Copy the generated code from the interface
2. Save it to a `.py` file (e.g., `my_video.py`)
3. Run with Manim:
   ```bash
   manim my_video.py CombinedVideo -pql
   ```
4. Find your video in the `media/videos` folder

## Interface Features

### Smart Input Validation
- Ensures either PDF or text input is provided
- Validates API key availability
- Provides helpful error messages

### Real-time Feedback
- Progress updates during processing
- Detailed error messages if processing fails
- Comprehensive statistics on completion

### Professional UI
- Clean, modern interface
- Responsive design
- Helpful instructions and tooltips

## Configuration

### Environment Variables

Set these in your `.env` file or environment:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Customization

The frontend can be customized by modifying `gradio_app.py`:

- **Port**: Change `server_port` in the `launch()` call
- **Styling**: Modify the `custom_css` variable
- **Layout**: Adjust the Gradio components in `create_interface()`

## API Integration

The frontend integrates with the core pipeline through:

```python
from data_processing.multi_scene_processor import process_large_document

multi_scene, generated_code = process_large_document(
    pdf_path=pdf_file_path,
    pdf_bytes=pdf_bytes_object,
    text_input=text_content,
    document_title=title,
    api_key=api_key
)
```

## Troubleshooting

### Common Issues

1. **"No API key provided"**
   - Set `GOOGLE_API_KEY` environment variable, or
   - Provide API key directly in the interface

2. **"Please provide either a PDF file or text input"**
   - Upload a PDF file, or
   - Enter text in the text input field

3. **Processing fails**
   - Check API key validity
   - Ensure input content is readable
   - Check console output for detailed error messages

### Performance Notes

- Large PDFs may take longer to process
- Text input processing is typically faster
- Complex documents generate more detailed scenes

## Development

### File Structure

```
frontend/
├── gradio_app.py     # Main Gradio application
├── README.md         # This documentation
└── ...

run_frontend.py       # Simple launcher script
```

### Extending the Frontend

To add new features:

1. Modify `ManimPipelineFrontend` class in `gradio_app.py`
2. Add new input components in `create_interface()`
3. Update the `process_input()` method to handle new parameters
4. Test thoroughly with various input types

## Support

For issues and questions:
- Check the main project README
- Review error messages in the interface
- Ensure all dependencies are installed correctly
- Verify API key configuration
