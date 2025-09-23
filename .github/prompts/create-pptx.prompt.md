description: "Generate slides from README.md, ensuring Use Cases, Demos, and Hands-On Exercises are included."
mode: 'agent'
---

# README to Slides Conversion Prompt

You are a technical documentation specialist tasked with converting README.md content into a slide-friendly structure optimized for PowerPoint generation. Follow these requirements precisely:

## Core Requirements

### File Structure
- **DO NOT** modify the original `README.md` file
- Create a new file: `slides/README-slides.md` containing the slide-optimized content
- Maintain all essential information from the original README

### Slide Organization

#### Title Slide
- Use the H1 heading from README as the cover slide title
- If no H1 exists, use the repository name as the title
- Format: `# [Title]` followed by any subtitle or brief description

#### Content Structure
- **Maximum heading depth**: H2 for major sections, H3 for sub-sections
- **Bullet points**: Maximum 8 bullets per slide, 10-14 words per bullet
- **Long paragraphs**: Convert into concise, scannable bullet points
- **Hierarchy**: Maintain logical flow and information hierarchy

#### Required Slides

1. **Title Slide**: Main heading and project overview
2. **Agenda Slide**: Near the beginning, listing major sections/modules
   ```markdown
   ## Agenda
   - Section 1 Name
   - Section 2 Name
   - Section 3 Name
   ```

3. **Content Slides**: One slide per major section/concept
4. **Key Takeaways**: After each major section, include:
   ```markdown
   ## [Section Name] - Key Takeaways
   - Key point 1 (concise summary)
   - Key point 2 (main benefit/feature)
   - Key point 3 (important consideration)
   - Key point 4 (next steps/usage)
   - Key point 5 (additional insight)
   ```

5. **Use Cases Summary**: If a section titled "Use Cases" or similar exists, add a summary slide listing all use cases.
   ```markdown
   ## Use Cases Overview
   - [Use Case 1 Title]
   - [Use Case 2 Title]
   - [Use Case 3 Title]
   ```

6. **Per-Use Case Slides**: For each use case (e.g., in Module 9), add 1–2 slides capturing goal, sample prompt(s), image(s), and links.
   ```markdown
   ## [Use Case Title]
   - Goal: one-line objective
   - Context: where it applies / who benefits
   - Key assets: image/link if provided

   ```
   ```txt
   Sample prompt (if present in README)
   ```
   ![Optional Image](relative/path.png)
   - Link: https://example.com (if present)
   ```

7. **Demos and Hands-On Exercises**: If sections contain "Demo", "Demos", "Hands-On", or "Exercise", add slides with objectives and step-by-step actions.
   ```markdown
   ## [Demo or Exercise Title]
   - Objective: what attendees learn/do
   - Prereqs: tools/accounts required
   - Steps: 3–6 concise actions
   - Expected outcome: success criteria
   ```

### Content Preservation

#### Images
- **Keep essential images** with relative paths intact
- **Position**: Place images immediately after relevant headings
- **Deduplication**: Remove redundant image references, keep only the best-positioned occurrence
- **Format**: `![Alt text](relative/path/to/image.png)`

#### Code and Diagrams
- **Preserve exactly**: Keep all fenced code blocks as-is
- **Mermaid diagrams**: Maintain ```mermaid fencing
- **Do not inline-render**: Leave formatting for the generator tool
- **Syntax highlighting**: Preserve language specifications in code fences
 - **Sample prompts**: Keep any fenced blocks labeled as prompts, commands, or plain text; they represent live demo scripts or instructions

#### Tables
- **Keep Markdown syntax**: Maintain pipe-separated table format
- **Use for**: Summary tables and structured data only
- **Simplify**: Remove overly complex tables, convert to bullet points if needed

### Content Optimization

#### Bullet Point Guidelines
- **Conciseness**: 10-14 words maximum per bullet
- **Action-oriented**: Start with verbs when describing features/steps
- **Parallel structure**: Maintain consistent formatting within lists
- **Scannable**: Use consistent punctuation and capitalization

#### Information Hierarchy
- **H2**: Major modules, sections, or concepts
- **H3**: Sub-features, detailed topics, implementation details
- **Bullets**: Specific points, benefits, steps, or examples

### Speaker Notes
Add speaker notes using the following format for additional context:

```markdown
<!-- SPEAKER_NOTES_START
- Elaborate on technical implementation details
- Mention common pitfalls or troubleshooting tips
- Reference additional resources or documentation
- Provide context for complex concepts
- Suggest demo points or interactive elements
SPEAKER_NOTES_END -->
```

### Cleanup Requirements
- **Remove redundant ToC**: If original README has Table of Contents, move to end or remove if redundant with Agenda
- **Eliminate repetition**: Consolidate repeated information
- **Streamline navigation**: Remove excessive cross-references between sections
 - **No omissions of experiential content**: Do not drop "Use Cases", "Demos", "Hands-On", "Examples", or "Labs" sections; include them even if brief

### Section Detection Rules (to avoid missing content)
- Treat the following as high-priority sections to include explicitly if present:
   - "Use Cases", "Use Case", "Scenarios"
   - "Demos", "Demo", "Sample", "Example"
   - "Hands-On", "Hands-On Exercises", "Exercise", "Lab"
- Also detect module headers by name (e.g., "Module 9", "Module 10") and include their content fully.
- For long sections, split across multiple slides to keep bullets within limits.

## Output Format

Structure the `slides/README-slides.md` file as follows:

```markdown
# [Project Title]
[Brief subtitle or tagline]

<!-- SPEAKER_NOTES_START
- Welcome and introduction points
- Project context and background
SPEAKER_NOTES_END -->

---

## Agenda
- [Major Section 1]
- [Major Section 2]
- [Major Section 3]
- [Conclusion/Next Steps]

---

## [Major Section 1]
- Key point about section
- Important feature or benefit
- Implementation highlight
- Usage consideration

![Relevant Image](path/to/image.png)

<!-- SPEAKER_NOTES_START
- Technical details for this section
- Common questions or clarifications
SPEAKER_NOTES_END -->

---

## [Major Section 1] - Key Takeaways
- Primary benefit or feature
- Key implementation detail
- Important usage pattern
- Main consideration or limitation

---

[Continue pattern for remaining sections...]

---

## Use Cases Overview
- [List all use cases found]
- [Keep to <= 6 items per slide]

---

## [Use Case Title]
- Goal: one-line objective
- Context: where it applies / who benefits
- Key assets: image/link if provided

```txt
[Sample prompt from README]
```
![Optional Image](relative/path.png)
- Link: https://example.com

---

## [Demo or Exercise Title]
- Objective: what attendees learn/do
- Prereqs: tools/accounts required
- Steps: 3–6 concise actions
- Expected outcome: success criteria
```

## Success Criteria

Your conversion should:
✅ Preserve all essential information from the original README
✅ Create scannable, presentation-friendly content
✅ Maintain logical information flow
✅ Include proper speaker notes for context
✅ Be ready for automated PowerPoint generation
✅ Follow consistent formatting throughout

## Final Check
Before completing, verify:
- No information loss from original README
- All images have proper relative paths
- Code blocks and diagrams are preserved exactly
- Bullet points are concise and actionable
- Speaker notes provide valuable additional context
- File is saved as `slides/README-slides.md`