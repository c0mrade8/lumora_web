import React from 'react';

const BlogCard = ({ blog }) => (
    <div className="blog-card shadow-sm p-4 mb-3 bg-white rounded border-0">
        <div className="d-flex justify-content-between align-items-center mb-2">
            <span className="badge rounded-pill px-3 py-2" style={{backgroundColor: '#e0f2f1', color: '#00796b'}}>
                {blog.mood || 'Reflective'}
            </span>
            <small className="text-muted">{new Date(blog.created_at).toLocaleDateString()}</small>
        </div>
        <h4 className="fw-bold" style={{color: '#2c3e50'}}>{blog.title}</h4>
        <p className="text-secondary">{blog.content.substring(0, 150)}...</p>
        <hr />
        <div className="d-flex align-items-center">
            <div className="avatar-circle me-2"></div> 
            <small className="fw-bold text-muted">@{blog.author_name}</small>
        </div>
    </div>
);

export default BlogCard;