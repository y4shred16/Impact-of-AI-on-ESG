import pandas as pd
import json

def save_to_csv(input_file, output_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    save_to_csv("examples/sample_response.json", "examples/esg_data.csv")
