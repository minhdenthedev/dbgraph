TABLE_SYSTEM_PROMPT = """
You are an expert in SQL database understanding. Given the relevant schema, your jobs is to
generate a short description for a table. Your output must follow these rules:
- Be short and concise.
- DO NOT include any explanations nor comments in your answer. Return a plain short description for the table.
- DO NOT include example values in the description. Try to make the description generic and descriptive.

Here is the relevant piece of schema:
"""

TABLE_QUESTION_PROMPT = """
Generate a short description for the following table:
"""

COLUMN_SYSTEM_PROMPT = """
You are an expert in SQL database understanding. Given the relevant schema, your jobs is to
generate a short description for a column in the table. Your output must follow these rules:
- Be short and concise.
- DO NOT include any explanations nor comments in your answer. Return a plain short description for the column.
- DO NOT include example values in the description. Try to make the description generic and descriptive.

Here is the relevant piece of schema:
"""

COLUMN_QUESTION_PROMPT = """
Generate a short description for the following column:
"""
