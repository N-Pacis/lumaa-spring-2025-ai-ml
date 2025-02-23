# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

## Dataset
- Source: TMDB 5000 Movie Dataset (filtered to the first 500 movies).
- Download: [movies.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

## Requirements
- Python 3.8+
- Libraries: pandas, scikit-learn

## Installation
```bash
pip install pandas scikit-learn
```

## Usage
```bash
python main.py "I love movies that combine action and drama and also that are engaging and also have a deep story."
```

## Example Output
| title              | overview                                                       | similarity |
|--------------------|----------------------------------------------------------------|------------|
| Oceans             | An ecological drama/documentary, filmed throug...              | 0.101187   |
| Mad Max: Fury Road | An apocalyptic story set in the furthest reach...              | 0.087644   |
| The Lovers         | The Lovers is an epic romance time travel adve...              | 0.087430   |
| Epic               | A teenager finds herself transported to a deep...              | 0.073938   |
| Cold Mountain      | In this classic story of love and devotion set...              | 0.072537   |

## Salary Expectation
$4000/month (Calculated as $25/hour).

## Video Demo
- [Watch Video Demo](https://www.loom.com/share/9df6b9ff5f434b1a9223d925a49212df?sid=6235e8b3-6573-4d42-a6f9-59ffa81ac981)  
- Shows code execution for query: "I love movies that combine action and drama and also that are engaging and also have a deep story."
- Outputs top 5 closestrecommendations with titles,overviews, and similarity score.