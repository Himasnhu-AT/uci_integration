import { Injectable } from '@nestjs/common';

@Injectable()
export class AuthService {
    status(): string {
        return "Hello World"
    }
}
