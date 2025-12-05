Simple URL Shortener

A small web application that takes long URLs and gives you a shorter, easy-to-share link. Built with Python (Flask) and SQLite, with a clean, responsive black & white UI.

⸻

Features
	•	Shorten long URLs with a unique code
	•	Redirect short URLs to the original URL
	•	Stores URL mapping in SQLite
	•	Responsive, clean UI (black background, white text)
	•	Works on desktop and mobile

⸻

How It Works
	1.	Enter a long URL in the input box
	2.	Click Shorten
	3.	A short URL is generated
	4.	Clicking the short URL redirects to the original URL

Note: Make sure to include https:// in your long URL if it’s missing.

⸻

Technologies Used
	•	Backend: Python + Flask
	•	Database: SQLite
	•	Frontend: HTML, CSS (responsive design)

Porject Structure

URL_Shortener/
│── app.py
│── database.db  (auto-created)
│── templates/
│     └── index.html
│── static/
      └── style.css

Future Improvements
	•	Add click analytics for short URLs
	•	Add QR code generation for each short URL
	•	Deploy online (e.g., Heroku, Vercel, Render)

⸻

Author
 PANKAJ -- A software Developer --
