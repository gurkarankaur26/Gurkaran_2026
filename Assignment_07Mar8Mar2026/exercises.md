Q1. You have two lists of numbers:
    Predicted values from a model
    [10.4, 7.4, 3.6]
    Actual values from real data
    [8, 3, 10]
    Each position corresponds to the same stock.
    Example:
    Stock1 → predicted 10.4, actual 8
    Stock2 → predicted 7.4, actual 3
    Stock3 → predicted 3.6, actual 10

    What needs to be done:
    You must compare these two lists and produce one single number that represents how wrong the predictions are.

    So the requirement is:
    Measure the difference for each pair
    Compare predicted vs actual value at the same index.
    Combine all those differences into one number
    That number should represent the overall error of the model.
    The final result should be a decimal value, because prediction errors are usually fractional.

    In simple terms, the task is:
    You have two numeric lists of equal length
    Compare them element by element
    Create one metric (single number) that represents how different they are

    Key idea
    Design an error function (loss function) used in machine learning model training.



    Q2. Build a semantic product search engine using LLM embeddings—allow the user to describe what they are looking for, then return the top 3 closest products from a product list (which can be generated or downloaded, e.g., using ChatGPT or from the internet).

    Q3.  Build a system that, given a list of diseases and symptoms, finds and lists the closest disease based on user-entered symptoms using LLM embeddings.
    
    Q4. Build a search system that, given a paragraph or phrase entered by the user, finds and lists the closest page from a set of 1,000 pages (e.g., Wikipedia pages) using LLM embeddings.