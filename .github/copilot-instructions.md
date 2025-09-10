# AI Dev Tasks

When the user requests structured feature development, always follow these **3 mandatory steps** in order.  

The following files must be referenced during each step:

1. **Generate PRD**(Product Requirement Document)  
   - Command example:  
     ```
     Use @create-prd.md  
     Here's the feature I want to build: [Describe your feature in detail]  
     Reference these files to help you: [Optional: @file1.py @file2.ts]  
     ```  
   - You must use: `/ai-dev-tasks/create-prd.md`  
   - Output: A complete PRD document (e.g., `prd-user-profile-editing.md`)
	   - Output Format: Markdown (`.md`)
	   - Output Location: `/tasks/`
	   - Output Filename: `prd-[feature-name].md`

2. **Generate Task List**  
   - Command example:  
     ```
     Now take @prd-[feature-name].md and create tasks using @generate-tasks.md  
     ```  
   - You must use: `/ai-dev-tasks/generate-tasks.md` and `/tasks/prd-[feature-name].md`
   - Output: A structured task list based on the PRD  
	   - Output Format: Markdown (`.md`)
	   - Output Location: `/tasks/`
	   - Output Filename: `tasks-[prd-file-name].md` (e.g., `tasks-prd-user-profile-editing.md`)


3. **Process Task**  
   - Command example:  
     ```
     Please start on task 1.1 in @tasks-[prd-file-name].md and use @process-task-list.md  
     ```
     또는 한국어로  
     ```
     @process-task-list.md를 참고하여 @tasks-[prd-file-name].md에 정의된 1.1번 task를 처리해줘.
     ```  
   - You must use: `/ai-dev-tasks/process-task-list.md` and `/tasks/tasks-[prd-file-name].md`
   - Output: Processed result of the specified task  

---

## Notes
- The filenames in commands (`@prd-[feature-name].md`, `@tasks-[prd-file-name].md`,  and so on) may change depending on context, but the **workflow order must always remain the same**:  
  **PRD → Tasks → Process Tasks**  
- `@` means adding a particular file to the context. It may vary depending on the tool you are using.
- Always reference the correct base files in `/ai-dev-tasks/` when executing each step.