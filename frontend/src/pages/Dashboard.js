import React, { useEffect, useState } from 'react';
import api from '../api';
import BlogCard from '../components/Blogcard';

const Dashboard = () => {
    const [blogs, setBlogs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchBlogs = async () => {
            try {
                const response = await api.get('api/blogs/');
                setBlogs(response.data);
            } catch (err) {
                setError("Unable to connect to the safe space.");
            } finally {
                setLoading(false);
            }
        };
        fetchBlogs();
    }, []);

    if (loading) return <div className="loading-spinner">Calming the waters...</div>;
    if (error) return <div className="alert alert-warning m-5">{error}</div>;

    return (
        <div className="dashboard-container container mt-4">
            <header className="d-flex justify-content-between align-items-center mb-5">
                <h2 className="fw-light">Community <span className="fw-bold">Reflections</span></h2>
                <button className="btn btn-success rounded-pill px-4">Write a Post</button>
            </header>

            <div className="row">
                {blogs.length > 0 ? (
                    blogs.map(blog => (
                        <div key={blog.id} className="col-md-6 col-lg-4">
                            <BlogCard blog={blog} />
                        </div>
                    ))
                ) : (
                    <div className="text-center mt-5 p-5 bg-white rounded shadow-sm">
                        <h5>It's very quiet here...</h5>
                        <p className="text-muted">Be the first to share an anonymous thought.</p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Dashboard;