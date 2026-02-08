from bs4 import BeautifulSoup
import re
import os

def html_to_markdown(html_file_path, output_file_path):
    """
    Convert HTML file to Markdown format, preserving links and images.
    
    Args:
        html_file_path (str): Path to the input HTML file
        output_file_path (str): Path to the output Markdown file
    """
    
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title
    title = soup.find('title')
    title_text = title.get_text() if title else "Databricks Resources"
    
    # Start building markdown content
    markdown_content = f"# {title_text}\n\n"
    markdown_content += "## Databricks Resources and References\n\n"
    
    # Find the table with class 'tg'
    table = soup.find('table', class_='tg')
    
    if not table:
        print("No table with class 'tg' found")
        return
    
    # Process each table row
    rows = table.find_all('tr')
    
    for row in rows:
        cells = row.find_all('td')
        
        if len(cells) >= 2:
            # First cell contains the main link
            first_cell = cells[0]
            second_cell = cells[1]
            
            # Extract main link
            main_link = first_cell.find('a')
            if main_link:
                link_url = main_link.get('href', '#')
                link_text = main_link.get_text().strip()
                
                # Get description from second cell
                description_parts = []
                
                # Extract text content (excluding image links)
                for content in second_cell.contents:
                    if hasattr(content, 'name'):
                        if content.name == 'a' and content.find('img'):
                            # Skip image links for now, we'll handle them separately
                            continue
                        elif content.name in ['br']:
                            description_parts.append('\n')
                        elif content.name == 'li':
                            description_parts.append(f"- {content.get_text().strip()}\n")
                        elif content.name == 'ul':
                            # Handle unordered lists
                            for li in content.find_all('li'):
                                description_parts.append(f"- {li.get_text().strip()}\n")
                        else:
                            text = content.get_text().strip() if hasattr(content, 'get_text') else str(content).strip()
                            if text:
                                description_parts.append(text)
                    else:
                        # Text node
                        text = str(content).strip()
                        if text and text != '\n':
                            description_parts.append(text)
                
                description = ''.join(description_parts).strip()
                
                # Clean up description
                description = re.sub(r'\n+', '\n', description)
                description = re.sub(r'^\n|\n$', '', description)
                
                # Add main link and description to markdown
                markdown_content += f"- [{link_text}]({link_url})"
                
                if description:
                    markdown_content += f"| {description}"
                
                # Extract and add images
                image_links = second_cell.find_all('a', {'data-lightbox': True})
                
                if image_links:
                    markdown_content += " | "
                    
                    for img_link in image_links:
                        img = img_link.find('img')
                        if img:
                            img_src = img.get('src', '')
                            img_alt = img.get('alt', 'image')
                            img_title = img_link.get('data-title', img_alt)
                            
                            # Convert relative path to absolute if needed
                            if img_src.startswith('../'):
                                # Assuming the markdown file will be in the same directory structure
                                img_src = img_src.replace('../', './')
                            
                            markdown_content += f"![{img_alt}]({img_src} \"{img_title}\") "
                    
                    markdown_content += "\n\n"
                
                markdown_content += "---\n\n"
    
    # Write to markdown file
    os.makedirs(os.path.dirname(output_file_path) if os.path.dirname(output_file_path) else '.', exist_ok=True)
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    
    print(f"Markdown file created successfully: {output_file_path}")

def main():
    """Main function to run the converter"""
    
    # Define file paths
    html_file_path = "/Users/inbravo/GitHub/inbravo.github.io/html/databricks.html"
    output_file_path = "/Users/inbravo/GitHub/inbravo.github.io/md/databricks.md"
    
    # Check if input file exists
    if not os.path.exists(html_file_path):
        print(f"HTML file not found: {html_file_path}")
        return
    
    try:
        html_to_markdown(html_file_path, output_file_path)
    except Exception as e:
        print(f"Error converting HTML to Markdown: {str(e)}")

if __name__ == "__main__":
    # Install required package if not already installed
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("Installing required package: beautifulsoup4")
        import subprocess
        subprocess.check_call(["pip", "install", "beautifulsoup4"])
        from bs4 import BeautifulSoup
    
    main()