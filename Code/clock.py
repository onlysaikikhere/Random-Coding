def past(h, m, s):
    h_ms= h*60*60*1000 
    m_ms = m*60*1000
    s_ms = s*1000
    return (h_ms + m_ms + s_ms)

