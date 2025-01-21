# extract python code from research_results.md to generated_code.py
grep -A 1000 '```python' research_results.md | grep -B 1000 '```' | grep -v '```' > generated_code.py
