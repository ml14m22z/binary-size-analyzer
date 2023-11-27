# Change the page name of the output xlsx file

```markdown
    ml14m22z: Change the page name of the output xlsx file

    GitHub Copilot: To change the sheet name of the output Excel file, you can pass the `sheet_name` parameter to the `to_excel` function. Here's how you can do it:

    ```python
    df.to_excel(filename, index=True, sheet_name='Your Sheet Name')
    ```

    Replace `'Your Sheet Name'` with the name you want to give to the sheet.
```