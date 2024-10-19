import re
import pkg_resources

# Read the original requirements.txt file
with open("requirements.txt", "r") as file:
    lines = file.readlines()

# Create a new list to hold cleaned-up lines
cleaned_lines = []

# Pattern to match entries with @ file:///
pattern = re.compile(r"(.+?)\s*@\s*file://")

for line in lines:
    # Check if the line matches the pattern
    match = pattern.match(line)
    if match:
        package = match.group(1)
        try:
            # Get the installed version of the package
            version = pkg_resources.get_distribution(package).version
            # Add the package and version to the cleaned lines
            cleaned_lines.append(f"{package}=={version}\n")
        except pkg_resources.DistributionNotFound:
            # If the package is not found, keep the original line
            cleaned_lines.append(line)
    else:
        # Keep lines that don't match the pattern
        cleaned_lines.append(line)

# Write the cleaned lines to a new requirements.txt file
with open("cleaned_requirements.txt", "w") as file:
    file.writelines(cleaned_lines)

print("Cleaned requirements saved to cleaned_requirements.txt")

