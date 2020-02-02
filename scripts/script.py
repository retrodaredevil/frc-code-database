#!/usr/bin/env python3
import argparse
import datetime
import os
import sys
from pathlib import Path
import re


def root_path():
    return Path(Path(__file__).parent, "../")


def execute(command):
    return os.system(command)


def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def add(team, year, repo):
    print("team={} year={} repo={}".format(team, year, repo))
    path = Path(root_path(), "frc/{}/{}/".format(team, year)).absolute().resolve()
    path.mkdir(parents=True, exist_ok=True)
    code = execute("cd {} && git submodule add {}".format(path, repo))
    if code != 0:
        print("Unsuccessful with exit code={}".format(code))
    return code


def firstwiki_populate(args):
    exported = Path(root_path(), "scripts/firstwiki/data/exported")
    for file in exported.iterdir():
        name = file.name
        team = name.split(".")[0]
        try:
            team = int(team)
        except ValueError:
            continue
        with file.open('r') as f:
            content = "".join(f.readlines())
        split_content = content.split("robot_code:\n")
        if len(split_content) > 1:
            print(team)
            code_lines = split_content[1].split("\n")
            year = None
            for line in code_lines:
                if line.startswith(" " * 4):
                    line = line[4:]
                    if line.startswith("- "):
                        line = line[2:]
                        if validate_url(line):
                            add(team, year, line)
                elif line.startswith(" " * 2):
                    line = line[2:]
                    if not line.startswith("- "):
                        try:
                            year = int(line[:-1])
                        except ValueError:
                            pass
                else:
                    break
            return


def quick_add(args):
    parser = argparse.ArgumentParser(description="Quickly adds a git repository as a submodule")
    parser.add_argument('-t', '--team', help="The team number", required=True)
    parser.add_argument('-y', '--year', help="The year of the repo or 'other'.", required=True)
    parser.add_argument('-r', '--repo', help="The repository", required=True)
    parsed = parser.parse_args(args)
    team = parsed.team
    year = parsed.year
    repo = parsed.repo

    if year != "other":
        try:
            year_number = int(year)
        except ValueError:
            print("{} is not a valid year!".format(year))
            return
        if year_number < 1992:
            print("{}? That's impossible!".format(year))
            return
        current_year = datetime.datetime.now().year
        if year_number > current_year + 1:
            print("{}? That's too far in the future!".format(year))
            return
    try:
        team_number = int(team)
    except ValueError:
        print("{} is not a valid team!".format(team))
        return
    if team_number < 0 or team_number > 9999:
        print("{} is not a valid team!".format(team_number))
        return
    code = add(team, year, repo)
    exit(code)


def main():
    args = sys.argv[1:]
    if args:
        program = args[0].lower()
    else:
        program = None

    if program == "quick":
        quick_add(args[1:])
    elif program == "populate":
        firstwiki_populate(args[1:])
    else:
        if not program:
            print("You must specify a program type! quick|populate")
        else:
            print("{} is not a valid program. quick|populate".format(program))


if __name__ == '__main__':
    main()
