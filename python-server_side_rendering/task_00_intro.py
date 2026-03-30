fields = ["name", "event_title", "event_date", "event_location"]

def generate_invitations(template, attendees):
    """Generates the invitations for an event based on a template and attendee data.
    
    Parameters:
        template (str): The template to use for the invitations.
        attendees (list[dict]): Attendee data."""

    if not isinstance(template, str):
        raise TypeError("Template must be a string.")
    
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        raise TypeError("Attendees must be a list of dictionaries.")
    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    if len(attendees) < 1:
        print("No data provided, no output files generated.")
        return
    
    for i, attendee in enumerate(attendees):
        output = template

        for field in fields:
            val = "N/A"

            if field in attendee:
                val = attendee[field]
            
            output.replace(f"{{{field}}}", str(val))
        
        filename = f"output_{i + 1}.txt"
        
        with open(filename) as f:
            f.write(output)
