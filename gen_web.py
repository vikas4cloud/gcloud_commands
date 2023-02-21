import subprocess

url = "https://cloud.google.com/sdk/gcloud/reference/"
with open("gcloud_commands") as file:
	for x in file:
		line = x
		line = line.replace("gcloud ", "")
		line = line.replace("\n", "")
		updatedLine = ""
		lineSplit = line.split(" ")
		if " " in line:
			for x in lineSplit:
				updatedLine += x + "/"
		else:
			updatedLine = line + "/"
		if len(updatedLine) > 0:
			updatedLine = updatedLine[:-1]
		fullUrl = url + updatedLine
		outputfile = updatedLine + ".html"
		outputfile = outputfile.replace("/", "_")
		outputfile = "web/" + outputfile
		subprocess.call(["curl", "-o", outputfile, "--create-dirs", fullUrl])
