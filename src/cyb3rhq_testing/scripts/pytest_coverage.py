import argparse
import re
import subprocess
from os import chdir, remove
from os.path import basename, exists, join, dirname

PYTHON_MODULES = (
    'framework',  # Framework
    'api/api',  # API
    'wodles',  # External modules
    'integrations'  # Integrations
)

COVERAGE_FILE = '.coverage'
COVERAGE_REPORT = ''
COVERAGE_REGEX = r'^([\w\/._-]+) +(\d+) +(\d+) +(\d+)\%$'
GLOBAL_STMTS = 0
GLOBAL_MISS = 0
TABLE_HEADER = """| | | | | |
|--|--|--|--|--|
| **Name** | **Stmts** | **Miss** | **Cover** | **Status** |
"""


def obtain_coverage(module):
    chdir(dirname(module))
    module_basename = basename(module)

    module_report = f'### {module_basename.upper()}\n\n{TABLE_HEADER}'
    subprocess.run(['coverage', 'run', '--omit=*test*', '--source', module_basename,
                    '-m', 'pytest', module_basename],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    coverage_result = subprocess.check_output(['coverage', 'report']).decode().strip()
    test_coverage_results = re.findall(COVERAGE_REGEX, coverage_result, re.MULTILINE)
    for test in test_coverage_results:
        # test_name stmts miss cover
        coverage = int(test[3])
        if coverage >= 75:
            check = ':green_square:'
        elif coverage >= 50:
            check = ':yellow_square:'
        elif coverage >= 25:
            check = ':orange_square:'
        else:
            check = ':red_square:'

        module_report = f'{module_report}| {test[0]} | {test[1]} | {test[2]} | {coverage}% | {check} |\n'

    global COVERAGE_REPORT
    COVERAGE_REPORT = f'{COVERAGE_REPORT}{module_report}\n'

    global GLOBAL_STMTS, GLOBAL_MISS
    GLOBAL_STMTS += int(test_coverage_results[-1][1])
    GLOBAL_MISS += int(test_coverage_results[-1][2])

    # Remove .coverage file
    exists(COVERAGE_FILE) and remove(COVERAGE_FILE)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Pytest Coverage (Cyb3rhq)')
    parser.add_argument('-p', '--path', dest='cyb3rhq_path', action='store', required=True,
                        help='Path to the Cyb3rhq repository.')

    return parser.parse_args()


def main():
    arguments = parse_arguments()
    cyb3rhq_path = arguments.cyb3rhq_path

    if not exists(cyb3rhq_path):
        print(f'Base Cyb3rhq path is not valid: {cyb3rhq_path}')
        exit(1)

    for module in PYTHON_MODULES:
        current_module_path = join(cyb3rhq_path, module)

        if not exists(current_module_path):
            print(f'Cyb3rhq module path is not valid: {current_module_path}')
            exit(1)

        obtain_coverage(current_module_path)

    print(COVERAGE_REPORT)
    print(f'\nOVERALL COVERAGE PERCENTAGE: {100 - int(GLOBAL_MISS * 100 / GLOBAL_STMTS)}%')


if __name__ == '__main__':
    main()
