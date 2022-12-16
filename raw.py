import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtGui import QTextCursor


class ChatbotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # Set the window properties
        self.setGeometry(300, 300, 400, 340)
        self.setWindowTitle('Chatbot')
        self.show()
    
    def initUI(self):
        # Create the layout for the window
        layout = QVBoxLayout()

        # Create the text edit for displaying the output
        self.outputTextEdit = QTextEdit()
        self.outputTextEdit.setReadOnly(True)

        # Create the line edit for entering the user commands
        self.inputLineEdit = QLineEdit()

        # Create the button for sending the user commands
        self.sendButton = QPushButton("Send")
        self.sendButton.clicked.connect(self.handle_submit)

        # Create the layout for the input line edit and send button
        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.inputLineEdit)
        inputLayout.addWidget(self.sendButton)

        # Add the output text edit and input layout to the main layout
        layout.addWidget(self.outputTextEdit)
        layout.addLayout(inputLayout)

        # Set the layout for the window
        self.setLayout(layout)
        
    def handle_submit(self):
        # Get the command from the input field
        command = self.inputLineEdit.text()

        # Clear the input field
        self.inputLineEdit.setText('')

        # Add the command to the output
        self.outputTextEdit.moveCursor(QTextCursor.End)
        self.outputTextEdit.insertPlainText(f'User: {command}\n')

        # Perform the action and get the result
        result = self.perform_action(command)

        # Add the result to the output
        self.outputTextEdit.moveCursor(QTextCursor.End)
        self.outputTextEdit.insertPlainText(f'Bot: {result}\n')

    def perform_action(self, command):
        # Implement the logic for performing the action specified by the command here
        # For example, you can use a dictionary to map commands to functions
        # and call the appropriate function based on the command
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbotWindow = ChatbotWindow()
    sys.exit(app.exec_())
