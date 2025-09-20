from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Configuration
app.config['DEBUG'] = True

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/certifications')
def certifications():
    """Certifications page route"""
    certifications_data = [
        {
            'name': 'eJPT (eLearnSecurity Junior Penetration Tester)',
            'issuer': 'INE Security',
            'description': 'Practical penetration testing certification covering vulnerability assessment and exploitation',
            'icon': '🛡️',
            'level': 'Advanced'
        },
        {
            'name': 'eWPT (eLearnSecurity Web Application Penetration Tester)',
            'issuer': 'INE Security',
            'description': 'Advanced web application security testing and vulnerability assessment',
            'icon': '🌐',
            'level': 'Expert'
        },
        {
            'name': 'ICCA (INE Certified Cloud Associate)',
            'issuer': 'INE Security',
            'description': 'Cloud security fundamentals and best practices certification',
            'icon': '☁️',
            'level': 'Professional'
        },
        {
            'name': 'CC (Certified in Cybersecurity)',
            'issuer': 'ISC2',
            'description': 'Foundational cybersecurity principles and practices',
            'icon': '🔐',
            'level': 'Professional'
        }
    ]
    return render_template('certifications.html', certifications=certifications_data)

@app.route('/services')
def services():
    """Services page route"""
    services_data = [
        {
            'title': 'Penetration Testing',
            'description': 'Comprehensive security assessments to identify vulnerabilities in your systems',
            'icon': '🔍',
            'features': ['Network Penetration Testing', 'Web Application Testing', 'Mobile App Security', 'Wireless Security Assessment']
        },
        {
            'title': 'Security Consulting',
            'description': 'Strategic cybersecurity guidance to strengthen your security posture',
            'icon': '💼',
            'features': ['Security Policy Development', 'Compliance Assessment', 'Risk Management', 'Security Architecture Review']
        },
        {
            'title': 'Incident Response',
            'description': 'Rapid response and forensic analysis for security incidents',
            'icon': '🚨',
            'features': ['Malware Analysis', 'Digital Forensics', 'Breach Investigation', '24/7 Emergency Response']
        },
        {
            'title': 'Training & Awareness',
            'description': 'Cybersecurity training programs for organizations and individuals',
            'icon': '🎓',
            'features': ['Security Awareness Training', 'Technical Workshops', 'Certification Prep', 'Custom Training Programs']
        }
    ]
    return render_template('services.html', services=services_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Basic validation
        if not all([name, email, subject, message]):
            flash('Please fill in all fields.', 'error')
            return render_template('contact.html')
        
        # Here you would typically send an email or save to database
        # For now, we'll just show a success message
        flash(f'Thank you {name}! Your message has been received. I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/projects')
def projects():
    """Projects page route"""
    projects_data = [
        {
            'title': 'Enterprise Security Assessment',
            'description': 'Comprehensive security audit for a Fortune 500 company, identifying critical vulnerabilities and providing remediation strategies.',
            'technologies': ['Nmap', 'Burp Suite', 'Metasploit', 'OWASP ZAP'],
            'status': 'Completed',
            'category': 'Penetration Testing'
        },
        {
            'title': 'Web Application Security Framework',
            'description': 'Developed a custom security testing framework for automated vulnerability assessment of web applications.',
            'technologies': ['Python', 'Flask', 'SQLAlchemy', 'Docker'],
            'status': 'In Progress',
            'category': 'Development'
        },
        {
            'title': 'Cloud Security Migration',
            'description': 'Led the secure migration of critical infrastructure to AWS cloud with comprehensive security controls.',
            'technologies': ['AWS', 'Terraform', 'CloudTrail', 'IAM'],
            'status': 'Completed',
            'category': 'Cloud Security'
        },
        {
            'title': 'Incident Response Playbook',
            'description': 'Created detailed incident response procedures and automated tools for rapid threat detection and mitigation.',
            'technologies': ['SIEM', 'Splunk', 'Python', 'PowerShell'],
            'status': 'Completed',
            'category': 'Incident Response'
        }
    ]
    return render_template('projects.html', projects=projects_data)

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)