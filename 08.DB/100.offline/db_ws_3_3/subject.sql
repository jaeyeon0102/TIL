USE online_course_platform_db

SELECT f.comment 
FROM feedback f 
WHERE student_id = (SELECT id FROM students WHERE username = 'john_doe')
ORDER BY created_at ASC
LIMIT 1;

CREATE VIEW 
  student_feedback_with_courses AS
SELECT 
  s.username AS username,
  c.title AS course_title,
  f.comment,
  f.created_at
  FROM feedback f 
  JOIN students s ON s.id = f.student_id 
  JOIN courses c ON c.id = f.course_id

SELECT *
FROM student_feedback_with_courses
WHERE username = 'john_doe'