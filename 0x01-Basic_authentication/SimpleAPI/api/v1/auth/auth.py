#!/usr/bin/env python3
""" Auth """

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if the path requires authentication."""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        authorization = request.headers.get('Authorization')
        if request is None or authorization is None:
            return None
        return authorization

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """current_user"""
        return None