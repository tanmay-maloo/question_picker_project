import json
import os
import random
from datetime import datetime
import shutil

class QuestionPicker:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def get_random_unsolved_question(self):
        data = self.load_data()
        not_suggested_questions = [
            q for item in data['sheetData'] for q in item['topics']
            if q.get('status', 'Not Suggested') in ['Not Suggested', 'Favorite']
        ]
        if not not_suggested_questions:
            return None
        random_question = random.choice(not_suggested_questions)
        if random_question.get('status', 'Not Suggested') == 'Not Suggested':
            random_question['status'] = 'Suggested'
            self.save_data(data)
        return random_question

    def mark_question_done(self, question_id):
        data = self.load_data()
        for item in data['sheetData']:
            for topic in item['topics']:
                if topic['id'] == question_id and topic.get('status') == 'Suggested':
                    topic['status'] = 'Done'
                    self.save_data(data)
                    return True
        return False

    def mark_question_favorite(self, question_id):
        data = self.load_data()
        for item in data['sheetData']:
            for topic in item['topics']:
                if topic['id'] == question_id and topic.get('status') == 'Suggested':
                    topic['status'] = 'Favorite'
                    self.save_data(data)
                    return True
        return False

    def get_favorite_questions(self):
        data = self.load_data()
        favorite_questions = []
        for item in data['sheetData']:
            topic_favorites = [q for q in item['topics'] if q.get('status') == 'Favorite']
            if topic_favorites:
                favorite_questions.append({
                    'topic': item['head_step_no'],
                    'questions': topic_favorites
                })
        return favorite_questions

    def get_topic_progress(self):
        data = self.load_data()
        progress = []
        for item in data['sheetData']:
            total = len(item['topics'])
            done = sum(1 for q in item['topics'] if q.get('status') == 'Done')
            progress.append({
                'topic': item['head_step_no'],
                'done': done,
                'total': total,
                'percentage': (done / total) * 100 if total > 0 else 0
            })
        return progress

    def reset_sheet(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        backup_file_name = f'dsa-sheet-{current_date}.json'
        backup_file_path = os.path.join(os.path.dirname(self.file_path), backup_file_name)
        shutil.copyfile(self.file_path, backup_file_path)
        
        data = self.load_data()
        for item in data['sheetData']:
            for topic in item['topics']:
                topic['status'] = 'Not Suggested'
        self.save_data(data)
        return backup_file_name

    def get_suggested_questions(self):
        data = self.load_data()
        return [q for item in data['sheetData'] for q in item['topics'] if q.get('status') == 'Suggested']