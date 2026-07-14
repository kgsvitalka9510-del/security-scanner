"""Security scanner."""

class Scanner:
    def scan(self, path: str):
        return ScanResult(issues=[])
    
class ScanResult:
    def __init__(self, issues):
        self.issues = issues
