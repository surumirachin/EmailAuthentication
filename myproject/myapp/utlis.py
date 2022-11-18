def handle_uploaded_file(file):

    with open(f"media/{file.name}", "wb+") as destination:

        for chunk in file.chunks():

            destination.write(chunk)