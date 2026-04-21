import re
import sys

def replace_lab_section(filepath, lab_heading_start, next_section_heading, new_content_file):
    """Replace everything from lab heading to next section heading with new content."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    with open(new_content_file, 'r') as f:
        new_lab = f.read()
    
    # Find the position of the lab section start
    lab_pos = content.find('\n## ' + lab_heading_start)
    if lab_pos == -1:
        # Try without leading newline
        lab_pos = content.find('## ' + lab_heading_start)
        if lab_pos == -1:
            print(f"ERROR: Could not find lab heading '{lab_heading_start}' in {filepath}")
            return False
    
    # Find the position of the next section
    next_pos = content.find('\n## ' + next_section_heading, lab_pos + 10)
    if next_pos == -1:
        # Also try with space before next heading
        print(f"ERROR: Could not find next section '{next_section_heading}' in {filepath}")
        return False
    
    # Replace section
    before = content[:lab_pos]
    after = content[next_pos:]
    
    new_content = before + '\n\n' + new_lab.strip() + '\n' + after
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"Replaced lab in {filepath}")
    return True


ASSETS = '/home/node/openclaw/books/vibe-marketing-martech/assets/'
CHAPTERS = '/home/node/openclaw/books/vibe-marketing-martech/chapters/'

replacements = [
    # (chapter file, lab heading fragment to find, next section heading fragment, new content file)
    (
        CHAPTERS + 'ch00-before-you-can-market.md',
        '0.7 Lab 0:',
        '0.8 Case Study',
        ASSETS + 'lab0_content.md'
    ),
    (
        CHAPTERS + 'ch01-vibe-revolution.md',
        '1.12 Lab 1:',
        '1.13 Chapter Takeaways',
        ASSETS + 'lab1_content.md'
    ),
    (
        CHAPTERS + 'ch02-funnels.md',
        '2.12 Lab 2:',
        '2.13 Chapter Takeaways',
        ASSETS + 'lab2_content.md'
    ),
    (
        CHAPTERS + 'ch03-pipelines.md',
        '3.10 Lab 3:',
        '3.11 Chapter Takeaways',
        ASSETS + 'lab3_content.md'
    ),
    (
        CHAPTERS + 'ch04-workflows.md',
        '4.13 Lab 4:',
        '4.14 Chapter Takeaways',
        ASSETS + 'lab4_content.md'
    ),
    (
        CHAPTERS + 'ch06-conversations.md',
        '6.12 Lab 6:',
        '6.13 Chapter Takeaways',
        ASSETS + 'lab6_content.md'
    ),
    (
        CHAPTERS + 'ch07-forms-documents-calendar.md',
        '7.16 Lab 7:',
        '7.17 Chapter Takeaways',
        ASSETS + 'lab7_content.md'
    ),
    (
        CHAPTERS + 'ch08-stripe-plaid.md',
        '8.11 Lab 8:',
        '8.12 Chapter Takeaways',
        ASSETS + 'lab8_content.md'
    ),
    (
        CHAPTERS + 'ch09-ai-employees.md',
        '9.9 Lab 9:',
        '9.10 Case Study',
        ASSETS + 'lab9_content.md'
    ),
    (
        CHAPTERS + 'ch10-reputation.md',
        '10.9 Lab 10:',
        '10.10 Reputation as a Sales Tool',
        ASSETS + 'lab10_content.md'
    ),
    (
        CHAPTERS + 'ch11-reporting.md',
        '11.8 Lab 11:',
        '11.9 Using Data',
        ASSETS + 'lab11_content.md'
    ),
    (
        CHAPTERS + 'ch12-social.md',
        '12.9 Lab 12:',
        '12.10 Social Media Best Practices',
        ASSETS + 'lab12_content.md'
    ),
]

success = 0
fail = 0
for (filepath, lab_heading, next_heading, new_file) in replacements:
    if replace_lab_section(filepath, lab_heading, next_heading, new_file):
        success += 1
    else:
        fail += 1

print(f"\nDone: {success} replaced, {fail} failed")
