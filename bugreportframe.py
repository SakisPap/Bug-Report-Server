def bugreport(parent, msg):
    try:
        message = urllib.parse.quote_plus(msg)
        req = urllib.request.Request("http://server.ddns.net/bugreport.php?bodyofmessage=" + message)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        urllib.request.urlopen(req)
        tk.messagebox.showinfo("Success!", "Bug report submitted successfully.\nThank you very much for your involvement!", parent=parent)
    except:
        tk.messagebox.showerror("Error", "Failed to send bug report.\n Check your internet connection and try again later.", parent=parent)
    parent.destroy()
    
    
window = tk.Toplevel(relief=tk.FLAT, highlightthickness=0)
window.geometry("445x210")
window.resizable(width=False, height=False)
window.title("Report Bug")
window.attributes('-topmost', 'true')
window.grab_set()

label = tk.Label(window, text="Please describe the issue with as many details as possible,\nprovide your contact info if you want us to reach you back.")
label.pack(pady=5)
reportEntry = tk.Text(window, font=("OpenSans", 9), width=60, height=8, wrap=tk.WORD)
reportEntry.pack(padx=10)

submit = tk.Button(window, text="Submit", command = lambda : [(label.config(text="Sending the report...\n", fg="black"), submit.config(text="Please wait..."), label.update(), submit.update(), bugreport(window, reportEntry.get("1.0", tk.END))) if not reportEntry.compare("end-1c", "==", "1.0") else label.config(text="Warning: You cannot submit an empty form!\n", fg="red")])
submit.pack(pady=10)

window.mainloop()
