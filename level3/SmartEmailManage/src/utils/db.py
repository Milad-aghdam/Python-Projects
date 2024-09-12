from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware


class DatabaseManager:
    def __init__(self, db_path='database.json'):
        # Initialize the database with caching middleware
        self.db = TinyDB(db_path, storage=CachingMiddleware(JSONStorage))
        
        # Initialize tables
        self.profiles_table = self.db.table('profiles')
        self.templates_table = self.db.table('templates')
        self.sent_emails_table = self.db.table('sent_emails')
        self.reminders_table = self.db.table('reminders')
        self.id_table = self.db.table('id_table')

        # Initialize IDs for different tables
        if not self.id_table.contains(Query().table_name == 'profiles'):
            self.id_table.insert({'table_name': 'profiles', 'last_id': 0})
        if not self.id_table.contains(Query().table_name == 'templates'):
            self.id_table.insert({'table_name': 'templates', 'last_id': 0})
        if not self.id_table.contains(Query().table_name == 'sent_emails'):
            self.id_table.insert({'table_name': 'sent_emails', 'last_id': 0})
        if not self.id_table.contains(Query().table_name == 'reminders'):
            self.id_table.insert({'table_name': 'reminders', 'last_id': 0})

    def _get_next_id(self, table_name):
        """Retrieve the next ID for a given table and increment the counter."""
        table_id = self.id_table.get(Query().table_name == table_name)
        next_id = table_id['last_id'] + 1
        self.id_table.update({'last_id': next_id}, Query().table_name == table_name)
        return next_id

    # Profile management
    def add_profile(self, email, name, title, profession):
        profile_id = self._get_next_id('profiles')
        self.profiles_table.insert({
            'id': profile_id,
            'email': email,
            'name': name,
            'title': title,
            'profession': profession
        })
        return profile_id

    def get_profiles(self):
        return self.profiles_table.all()

    def get_profile_by_email(self, email):
        Profile = Query()
        return self.profiles_table.search(Profile.email == email)

    # Template management
    def add_template(self, template_name, template_body):
        template_id = self._get_next_id('templates')
        self.templates_table.insert({
            'id': template_id,
            'template_name': template_name,
            'template_body': template_body
        })
        return template_id

    def get_templates(self):
        return self.templates_table.all()

    def get_template_by_name(self, template_name):
        Template = Query()
        return self.templates_table.search(Template.template_name == template_name)

    # Sent email management
    def save_sent_email(self, to, template_used, status, timestamp):
        email_id = self._get_next_id('sent_emails')
        self.sent_emails_table.insert({
            'id': email_id,
            'to': to,
            'template_used': template_used,
            'status': status,
            'timestamp': timestamp
        })
        return email_id

    def get_sent_emails(self):
        return self.sent_emails_table.all()

    def get_last_10_emails(self):
        # Assuming that emails are inserted in order, you can slice the last 10 entries
        return self.sent_emails_table.all()[-10:]

    # Reminder and schedule management
    def set_reminder(self, email_id, reminder_time):
        reminder_id = self._get_next_id('reminders')
        self.reminders_table.insert({
            'id': reminder_id,
            'email_id': email_id,
            'reminder_time': reminder_time
        })
        return reminder_id

    def get_reminders(self):
        return self.reminders_table.all()

    def get_upcoming_reminders(self):
        # Example function to filter reminders in the future
        return [reminder for reminder in self.reminders_table.all() if reminder['reminder_time'] > current_time]

    # Statistics or summary functions
    def get_email_statistics(self):
        return {
            'total_profiles': len(self.profiles_table),
            'total_templates': len(self.templates_table),
            'total_sent_emails': len(self.sent_emails_table),
            'total_reminders': len(self.reminders_table),
        }

