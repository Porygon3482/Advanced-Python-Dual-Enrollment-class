"""
Author: Neel Srivastava
Date: 18/5/26
Exercise: 14.1 - Retrieving WVC Schedule
Summary: The program retrieves the summer or fall semester west valley college directories
and put them in the local file system. Can also launch the web browser and see the file on the website
"""


import webbrowser
import requests

# Base URL for WVC schedule PDFs
BASE_URL = "https://www.westvalley.edu/documents/schedules/2026/"


def getFileChunk(url, localFileName):
    """
    Download a file from the given URL and save it locally, 16K bytes at a time.
    """

    #locates and downloads file
    with requests.get(url, stream=True) as response:
        response.raise_for_status()

        with open(localFileName, "wb") as schedule:
            for chunk in response.iter_content(chunk_size=16384):  # 16K bytes
                if chunk:  # filter out keep-alive chunks
                    schedule.write(chunk)

    print(f"Download complete! Saved as '{localFileName}'.")


def main():
    print("=" * 50)
    print("  West Valley College Schedule Downloader")
    print("=" * 50)

    # Ask the user which semester
    while True:
        semester = input("\nWhich semester would you like? (Summer / Fall): ").strip().lower()
        if semester == "summer":
            pdfFile = "Summer_26_Schedule.pdf"
            localFile = "Summer_2026_Schedule.pdf"
            break
        elif semester == "fall":
            pdfFile = "SuFa_26_Schedule_Full.pdf"
            localFile = "Fall_2026_Schedule.pdf"
            break
        else:
            print("Please enter 'Summer' or 'Fall'.")

    url = BASE_URL + pdfFile
    print(f"\nRetrieving: {url}")

    try:
        getFileChunk(url, localFile)
    except requests.exceptions.RequestException as e:
        print("Error downloading file:", e)
        return

    # Ask if the user wants to launch the web browser
    answer = input("\nWould you like to launch the web browser to view the file? (yes / no): ").strip().lower()
    if answer in ("yes", "y"):
        print(f"Opening: {url}")
        webbrowser.open(url)

    print("\nGoodbye!")


# -------- main program --------
if __name__ == "__main__":
    main()

