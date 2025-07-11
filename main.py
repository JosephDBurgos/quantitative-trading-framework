import argparse
from analysis.generate_moving_average_strategy_reports import generate_moving_average_reports
from analysis.analyze_moving_average_summary import analyze_moving_average_summary

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strategy', choices=['moving_average'], required=True)
    parser.add_argument('--analyze', action='store_true', help='Run analysis after report generation')
    args = parser.parse_args()

    if args.strategy == 'moving_average':
        generate_moving_average_reports()
        if args.analyze:
            analyze_moving_average_summary()

if __name__ == "__main__":
    main()