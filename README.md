# inventory
PES1UG23CS426 | SE Lab 5 | Section : G | Prajwal Gupta


SE Lab 5

**Name:** Prajwal Gupta

**SRN:** PES1UG23CS426

**Section:** G





**Issues with the code:**

| **Issue** | **Tool** | **Line(s)** | **Description** | **Fix Approach** |
| --- | --- | --- | --- | --- |
| **Missing module docstring** | pylint | 1   | No docstring at the top of the module | Add a brief description at the top of the file |
| **Missing function docstring** | pylint | 8,14,22,25,31,36,41,48 | No docstrings in functions | Add one-line docstring in every function |
| **Function name not in snake_case** | pylint | 8,14,22,25,31,36,41 | Function names use camelCase | Rename functions to snake_case (e.g., add_item, remove_item) |
| **Dangerous default value \[\]** | pylint | 8   | Mutable default argument | Use None as default and assign inside the function |
| **Consider using f-string** | pylint | 12  | Regular string formatting used | Change to f-string formatting |
| **No exception type specified** | pylint, flake8 | 19  | Bare except: used | Use except Exception: or a specific exception |
| **Using open without encoding** | pylint | 26,32 | open called without specifying encoding | Specify encoding='utf-8' and use with statement |
| **Using global statement** | pylint | 27  | Use of global variable | Avoid using global variables |
| **Consider using 'with' statement** | pylint | 26,32 | File operations not wrapped in with | Always use with open(...) as f: |
| **Use of eval** | pylint, bandit | 59  | Use of dangerous eval function | Replace with a safe alternative like ast.literal_eval (if possible) |
| **Unused import 'logging'** | pylint, flake8 | 2   | logging imported but never used | Remove the unused import from code |
| **Expected 2 blank lines** | flake8 | 8,14,22,25,31,36,41,48 | Functions not separated by 2 blank lines | Add appropriate blank lines between function definitions |
| **Expected blank lines after class/function** | flake8 | 61  | Function ends without required blank lines | Add 2 blank lines after the last function |
| **Try, Except, Pass detected** | bandit | 19  | Exception block only passes (no error handling) | Log, raise, or handle the exception instead of just pass |
| **Use safer function than eval** | bandit | 59  | eval considered insecure | Use ast.literal_eval for parsing literals, avoid eval for arbitrary code execution |

**Reflections:**

**Q1\] Which issues were the easiest to fix, and which were the hardest? Why?**

**Easiest Issues to Fix**

The formatting and structural issues were by far the easiest to resolve. Adding missing docstrings to functions was straightforward once I understood the required format. Each function needed a brief description of its purpose and parameters, which I could implement consistently across the codebase. Similarly, fixing the spacing issues (adding 2 blank lines between functions) was a quick mechanical fix that Flake8 and Pylint clearly pointed out.

Converting string formatting to f-strings was also relatively easy. The old \`.format()\` method calls were simple to identify and replace with the more readable f-string syntax. I appreciated how this change actually improved code readability while reducing character count.

**Hardest Issues to Fix**

The most challenging aspect was addressing the variable shadowing warnings (redefining names from outer scope). Initially, I thought these were false positives because the function parameters weren't truly conflicting with outer scope variables. However, pylint's concern made sense from a code clarity perspective-using identical parameter names at different scope levels can confuse readers. I had to systematically rename parameters (e.g., \`item\` → \`product_name\`, \`qty\` → \`quantity\`, \`filename\` → \`file_path\`) to improve code readability and follow best practices.

The \`global\` statement warning was also tricky because it highlighted a design consideration. While using globals works for a simple script, it is generally discouraged in larger projects. I understood that while the current approach is acceptable, it would be better to refactor the code structure in production applications to avoid relying on global state.

**Q2\] Did the static analysis tools report any false positives? If so, describe one example.**

Yes, I encountered what I initially considered a false positive with the variable shadowing warnings (W0621). When I first saw warnings like "Redefining name 'item' from outer scope," I was confused because my function parameters were clearly local to those functions.

Upon reflection, I realized this was not truly a false positive-it was a stylistic warning. The issue arose because in my initial code, I had variable names like \`item\` and \`qty\` appearing in multiple scopes (as loop variables, parameters, etc.). While Python handles this technically correctly, pylint was warning that using identical names could reduce code clarity. The tool was essentially saying, "This works, but it's not ideal practice."

This taught me that static analysis tools sometimes warn about things that technically work but could be improved for maintainability. It is valuable to distinguish between errors (things that do not work) and warnings (things that could be better). In this case, I chose to rename variables for clarity rather than suppress the warning.

**Q3\] How would you integrate static analysis tools into your actual software development workflow?**

I see static analysis tools as essential components of a disciplined development process. In my workflow, I would integrate them at multiple stages:

**Local Development:** Before committing code, I would run Pylint, Flake8, and Bandit locally. This habit would help catch issues early and maintain consistent code quality. I could even set up pre-commit hooks to automatically run these tools before allowing commits to the repository.

**Version Control Integration:** When pushing code to GitHub, I would set up continuous integration (CI) using GitHub Actions. This would automatically run static analysis tools on every pull request, ensuring that no low-quality code gets merged into the main branch. Developers would receive immediate feedback on their code without waiting for a manual code review.

**Build Pipeline:** In a professional setting, I would include these tools in the build process. If pylint score falls below a certain threshold (e.g., 8.0/10) or if Bandit detects security issues, the build would fail. This enforces a "quality gate" that must be passed before deployment.

**IDE Integration:** Setting up VSCode with pylint and other linters would give me real-time feedback while coding, similar to spell-checking in word processors. This would make the development experience smoother and more productive.

**Documentation:** I would document coding standards and the static analysis rules my team follows, ensuring consistency across the project and reducing debates about style.

**Q4\] What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**

**Improved Code Readability**:

The most noticeable improvement was in readability. After adding comprehensive docstrings, the code became self-documenting. Anyone reading the functions immediately understands their purpose, parameters, and return values without having to decipher the implementation. The f-strings made print statements and logging much clearer compared to the old \`.format()\` approach.

**Better Error Handling**

Replacing bare \`except:\` clauses with specific exceptions like \`KeyError\`, \`FileNotFoundError\`, and \`IOError\` made error handling more precise. The code now catches only the exceptions it expects, allowing unexpected errors to surface rather than being silently swallowed. This is crucial for debugging and understanding program behaviour.

**Enhanced Security**

The removal of the \`eval()\` function and replacement with \`ast.literal_eval()\` significantly improved security. The original code was vulnerable to arbitrary code execution through user input. The new approach safely evaluates only simple Python literals, protecting against malicious code injection.

**Improved Maintainability**

Clear naming conventions (snake_case for functions) and consistent function structure make the code easier to maintain and extend. Someone new to the project can quickly understand the codebase. The removal of variable shadowing also reduces cognitive load when reading the code.

**Consistency with Python Standards**

By adhering to PEP 8 standards through Flake8, the code now follows Python community conventions. This makes it more professional and ensures compatibility with other Python projects. When future developers (or my future self) read this code, it will feel familiar because it follows established patterns.

**Overall Quality Metrics**

The pylint score improved from 4.80/10 to 9.84/10, a remarkable increase that reflects genuine code quality improvements. While this is a numerical metric, it represents real progress in code structure, documentation, and adherence to best practices.

These improvements demonstrate that static analysis is not just about passing automated checks-it is about creating code that is secure, maintainable, and professional.
