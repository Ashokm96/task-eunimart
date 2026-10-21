from numbers import Real


SUPPORTED_OPERATIONS = {"sum", "subtract", "divide", "multiply"}


def calculate_operation(method, numbers):
    """Calculate an operation without external services or database side effects."""
    if method not in SUPPORTED_OPERATIONS:
        raise ValueError(f"Unsupported operation: {method}")
    if not numbers:
        raise ValueError("At least one number is required")
    if not all(isinstance(number, Real) and not isinstance(number, bool) for number in numbers):
        raise TypeError("All operands must be numbers")

    result = numbers[0]
    for number in numbers[1:]:
        if method == "sum":
            result += number
        elif method == "subtract":
            result -= number
        elif method == "divide":
            if number == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result /= number
        elif method == "multiply":
            result *= number
    return result


class Operations:
    def __init__(self, message):
        self.func_name = message["method"]
        self.number_list = message["list"]
        self.raw_content = message
        self.result = None

    def calculate(self):
        self.result = calculate_operation(self.func_name, self.number_list)
        self.save_message()
        return self.result

    def save_message(self):
        from sqlalchemy.exc import SQLAlchemyError
        from app import db
        from ..models.message import Message

        message = Message(self.func_name, self.raw_content, self.result)
        try:
            db.session.add(message)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise
