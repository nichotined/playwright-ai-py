# playwright-ai-py

This project is a Python based implementation for integrating Playwright with Open API and still in experimentation phase, not ready for any production use.  
This project aims to give you idea how AI can be integrated with Playwright to automate simple to complex tasks.

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
- It takes a long time to run the completion due to passing HTML source page to Open AI API call. Simple task can take up to X mins to complete. Hence, it is recommended to mix the implementation with calling Playwright API directly and then use OpenAI API for only certain part of the task.
- Limited to use OpenAI API, need to implement other providers.
- This uses `gpt-4o-mini` for the sake of cheap API price, which is not the best one. You may customized this by passing in the `model` parameter. 
- Not all Playwright functions are implemented yet, it can be extended by adding more functions in the `function_call.py` file, `action.py` file, and `constants/function_call.py` file.