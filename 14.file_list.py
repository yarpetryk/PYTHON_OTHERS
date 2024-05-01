import os
import re
import argparse
# ----------- os.listdir --------------
result = []
tracks = os.listdir('./')
for track in tracks:
    if "-" in track:
        print(track)
        track_name = re.split("\.", track)
        result.append(track_name[0])
print(result)

# --------------------argparse------------------------------------
def get_input_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description="Submit Nose2 Results to Azure Devops Test Plan.")
    parser.add_argument("--pat", type=str)
    parser.add_argument("--organization_url", type=str,
                        default="https://dev.azure.com/cosworth")
    parser.add_argument("--project_name", type=str, default="Software")
    parser.add_argument("--test_plan_area_path", type=str, default="AliveDrive\Performance\PDR 2.5\Embedded")
    parser.add_argument("--xml_path", type=str, default="nose2-junit.xml")
    parser.add_argument("--test_run_name", type=str)
    parser.add_argument("--pipeline_id", type=int)
    return parser.parse_args()


def main():
    input_args = get_input_args()
    project_name = input_args.project_name
    print(f"Arguments value -> '{project_name}'")

if __name__ == "__main__":
    main()