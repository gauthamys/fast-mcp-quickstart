from fastmcp import FastMCP

app = FastMCP(name="My FastMCP Server")

@app.tool("echo")
async def echo(request):
    data = await request.json()
    return {"echo": data}

@app.tool("test")
async def test(request):
    return {"status": "Test tool is working!"}

app = app.http_app(path="/api/mcp/")
