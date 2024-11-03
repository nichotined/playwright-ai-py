# playwright-ai-py

This project is a Python based implementation for integrating Playwright with Open API and still in experimentation phase, not ready for any production use.  

Check out the [main.py](main.py) file for an example of how to use it.

This project is inspired from the implementation of [auto-playwright](https://github.com/lucgagan/auto-playwright) in TypeScript.  

## Setup
```
poetry install
```
```
python main.py
```

## Known Issues
- Expensive token to run, need to be optimized the HTML cleaning part.
- It takes a long time to run the completion, need to optimize the code.
- Limited to use OpenAI API, need to implement other providers.