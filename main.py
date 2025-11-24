from pyscript import document, display

clubs = {
    "Fencing": {
        "Description": "A club that works on footwork and timing while blending in rapier fighting.",
        "Head": "John Borne",
        "Meeting Time": "Monday and Thursday 2:00-4:00PM",
        "Location": "Gymnasium",
        "Members": 9
    },
    "TKD": {
        "Description": "A club that encourages control with accuracy, precision, and speed.",
        "Head": "LePark",
        "Meeting Time": "Tuesday and Wednesday 2:30-4:00pm",
        "Location": "Gymnasium",
        "Members": 11
    },
    "Literary": {
        "Description": "A club for science experiments and discovery.",
        "Head": "Kimmy",
        "Meeting Time": "Monday and Tuesday 2:30-4:00 PM",
        "Location": "Room 805",
        "Members": 17
    }
}

def show_info(e):
    selected = document.getElementById('clubchoices').value
    club = clubs[selected]

    text = f"""
    <h3 class='club-title'>{selected} Club</h3>
    <p><strong>Description:</strong> {club["Description"]}</p>
    <p><strong>Meeting Time:</strong> {club["Meeting Time"]}</p>
    <p><strong>Location:</strong> {club["Location"]}</p>
    <p><strong>Head:</strong> {club["Head"]}</p>
    <p><strong>Number of Members:</strong> {club["Members"]}</p>
    """

    document.getElementById('output').innerHTML = text